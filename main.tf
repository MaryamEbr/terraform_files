provider "aws" {
  region = "us-west-2"
  profile = "default"
}

locals {
  serverconfig = [
    for srv in var.configuration : [
      for i in range(1, srv.no_of_instances+1) : {
        instance_name = "${srv.application_name}-${i}"
        instance_type = srv.instance_type
        subnet_id   = srv.subnet_id
        ami = srv.ami
        security_groups = srv.vpc_security_group_ids
      }
    ]
  ]
}

### flatten is needed for terraform purposes
locals {
  instances = flatten(local.serverconfig)
}

### aws ec2 instance building
resource "aws_instance" "early_exit" {
  for_each = {for server in local.instances: server.instance_name =>  server}

  ami = each.value.ami
  instance_type = each.value.instance_type
  vpc_security_group_ids = each.value.security_groups
  subnet_id = each.value.subnet_id
  key_name= "ee_key"
  source_dest_check = false
  tags = {
    Name = "${each.value.instance_name}"
  }

  ### to save the name and ips of current_tier inside of the instance
  provisioner "remote-exec" {
    
    inline = [
      "mkdir ins_folder",
      "mkdir ins_folder/files",
      "printf ${each.value.instance_name} >> ins_folder/files/current_tier.txt",
      "printf ^^^ >> ins_folder/files/current_tier.txt",
      "printf ${self.public_ip} >> ins_folder/files/current_tier.txt",
      "printf ^^^ >> ins_folder/files/current_tier.txt",
      "printf ${self.private_ip} >> ins_folder/files/current_tier.txt",

    ]
    
    connection {
      type        = "ssh"
      host        = self.public_ip
      user        = "ubuntu"
      private_key = file("ee_key.pem")
      timeout     = "4m"
    }
  }
  
}


### this outputs all information about instances to local machine (probably not needed)
output "instances" {
  value       = "${aws_instance.early_exit}"
  description = "All Machine details"
}

### this is to store the information of all created instances in files, after it's done
### because tiers need the ip of all other tiers for communications
### and this cannot be done in previsous block, it stucks in loop
resource "local_file" "local_file_store" {
  for_each = {for server in local.instances: server.instance_name =>  server}
  content = <<-EOL
    ${each.key}
    ${aws_instance.early_exit[each.key].public_ip}
    ${aws_instance.early_exit[each.key].private_ip}
    EOL
  filename = "ins_folder/files/terraform_info_${each.key}.txt"
}


### wait alittle bit to make sure files are ready before moving them to instances
### not sure if it's necessary
resource "time_sleep" "wait_30_seconds" {
  depends_on = [local_file.local_file_store]
  create_duration = "30s"
}

### transfer the folder with everything to instances
resource "null_resource" "transfering_files" {
  depends_on = [time_sleep.wait_30_seconds]
  for_each = {for server in local.instances: server.instance_name =>  server}

  provisioner "file" {


    source      = "ins_folder"
    destination = "/home/ubuntu/"

    connection {
      type        = "ssh"
      host        = aws_instance.early_exit[each.key].public_ip
      user        = "ubuntu"
      private_key = file("ee_key.pem")
      timeout     = "4m"
    }
  }
}


### again wait alittle bit to make sure files are ready 
resource "time_sleep" "wait_30_seconds2" {
  depends_on = [null_resource.transfering_files]
  create_duration = "30s"
}



#### Running the scripts and agents
resource "null_resource" "latency_bandwidth" {
  depends_on = [time_sleep.wait_30_seconds2]
  for_each = {for server in local.instances: server.instance_name =>  server}

  provisioner "remote-exec" {

    inline = [
      "chmod +x ins_folder/codes/routing_tc_script.py",
      "chmod +x ins_folder/codes/agent_source.py",
      "chmod +x ins_folder/codes/agent_inference.py",
      "chmod +x ins_folder/codes/agent_destination.py",
      # "ins_folder/codes/./routing_tc_script.py",
    ]

    connection {
      type        = "ssh"
      host        = aws_instance.early_exit[each.key].public_ip
      user        = "ubuntu"
      private_key = file("ee_key.pem")
      timeout     = "4m"
    }
  }
}