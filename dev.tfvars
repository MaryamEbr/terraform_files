configuration = [
  {
    "application_name" : "ee_tier1",
    "ami" : "ami-0d6e58541939104ee", ###Deep Learning AMI (Ubuntu 18.04) Version 60.1
    "instance_type" : "m4.xlarge", 
    "no_of_instances" : "1",
    "subnet_id" :"subnet-004d623e94d51414a" ###us-west-2a - Zone ID usw2-az2 - 172.31.0.0/20
    "vpc_security_group_ids" : ["sg-01f25add4086ca917"] ###default
  },
  {
    "application_name" : "ee_tier2",
    "ami" : "ami-0d6e58541939104ee", ###Deep Learning AMI (Ubuntu 18.04) Version 60.1
    "instance_type" : "m4.xlarge", 
    "no_of_instances" : "1"
    "subnet_id" : "subnet-004d623e94d51414a" ###us-west-2a - Zone ID usw2-az2 - 172.31.0.0/20
    "vpc_security_group_ids" : ["sg-01f25add4086ca917"] ###default
  },
  {
    "application_name" : "ee_tier3",
    "ami" : "ami-0d6e58541939104ee", ###Deep Learning AMI (Ubuntu 18.04) Version 60.1
    "instance_type" : "m4.xlarge", 
    "no_of_instances" : "1"
    "subnet_id" : "subnet-004d623e94d51414a" ###us-west-2a - Zone ID usw2-az2 - 172.31.0.0/20
    "vpc_security_group_ids" : ["sg-01f25add4086ca917"] ###default
  },
  {
    "application_name" : "ee_tier4",
    "ami" : "ami-0d6e58541939104ee", ###Deep Learning AMI (Ubuntu 18.04) Version 60.1
    "instance_type" : "m4.xlarge",
    "no_of_instances" : "1"
    "subnet_id" : "subnet-004d623e94d51414a" ###us-west-2a - Zone ID usw2-az2 - 172.31.0.0/20
    "vpc_security_group_ids" : ["sg-01f25add4086ca917"] ###default
  }
  
]

