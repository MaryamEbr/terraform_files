configuration = [
  {
    "application_name" : "ee_tier1",
    "ami" : "ami-0d6e58541939104ee", ###Deep Learning AMI (Ubuntu 18.04) Version 60.1
    "instance_type" : "t2.medium", ###vCPUs 2 -	i386, x86_64 - Memory 4G	- Network performance	Low to Moderate - Linux pricing	0.0464 USD per Hour
    "no_of_instances" : "1",
    "subnet_id" :"subnet-004d623e94d51414a" ###us-west-2a - Zone ID usw2-az2 - 172.31.0.0/20
    "vpc_security_group_ids" : ["sg-01f25add4086ca917"] ###default
  },
  {
    "application_name" : "ee_tier2",
    "ami" : "ami-0d6e58541939104ee", ###Deep Learning AMI (Ubuntu 18.04) Version 60.1
    "instance_type" : "t3.medium", ###vCPUs 2 -	x86_64 - Memory 4G	- Network performance	Up to 5 Gigabit - Linux pricing 0.0416 USD per Hour
    "no_of_instances" : "1"
    "subnet_id" : "subnet-004d623e94d51414a" ###us-west-2a - Zone ID usw2-az2 - 172.31.0.0/20
    "vpc_security_group_ids" : ["sg-01f25add4086ca917"] ###default
  },
  {
    "application_name" : "ee_tier3",
    "ami" : "ami-0d6e58541939104ee", ###Deep Learning AMI (Ubuntu 18.04) Version 60.1
    "instance_type" : "t3.large", ###vCPUs 2 -	x86_64 - Memory 8G	-  Network performance	Up to 5 Gigabit - Linux pricing 0.0832 USD per Hour
    "no_of_instances" : "1"
    "subnet_id" : "subnet-004d623e94d51414a" ###us-west-2a - Zone ID usw2-az2 - 172.31.0.0/20
    "vpc_security_group_ids" : ["sg-01f25add4086ca917"] ###default
  },
  {
    "application_name" : "ee_tier4",
    "ami" : "ami-0d6e58541939104ee", ###Deep Learning AMI (Ubuntu 18.04) Version 60.1
    "instance_type" : "t3.xlarge", ###vCPUs 4 -	x86_64 - Memory 16G	- Network performance	Up to 5 Gigabit - Linux pricing 0.1664 USD per Hour
    "no_of_instances" : "1"
    "subnet_id" : "subnet-004d623e94d51414a" ###us-west-2a - Zone ID usw2-az2 - 172.31.0.0/20
    "vpc_security_group_ids" : ["sg-01f25add4086ca917"] ###default
  }
  
]

