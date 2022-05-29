#!/Users/maryamebrahimi/.virtualenvs/uoftenv/bin/python3

import paramiko
import sys
import time
# sys.path.append('ins_folder/codes')
# import helper_functions


key = paramiko.RSAKey.from_private_key_file("ee_key.pem")

ssh1 = paramiko.SSHClient()
ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh1.connect(hostname="54.186.205.126", username="ubuntu", pkey=key)
sftp1 = ssh1.open_sftp()

ssh2 = paramiko.SSHClient()
ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh2.connect(hostname="34.212.53.85", username="ubuntu", pkey=key)
sftp2 = ssh2.open_sftp()

ssh3 = paramiko.SSHClient()
ssh3.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh3.connect(hostname="35.89.166.245", username="ubuntu", pkey=key)
sftp3 = ssh3.open_sftp()

ssh4 = paramiko.SSHClient()
ssh4.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh4.connect(hostname="34.219.202.222", username="ubuntu", pkey=key)
sftp4 = ssh4.open_sftp()


sftp1.put("ins_folder/files/destination_info.txt", "ins_folder/files/destination_info.txt")
sftp2.put("ins_folder/files/destination_info.txt", "ins_folder/files/destination_info.txt")
sftp3.put("ins_folder/files/destination_info.txt", "ins_folder/files/destination_info.txt")
sftp4.put("ins_folder/files/destination_info.txt", "ins_folder/files/destination_info.txt")

sftp1.put("ins_folder/files/partition_placement.txt", "ins_folder/files/partition_placement.txt")
sftp2.put("ins_folder/files/partition_placement.txt", "ins_folder/files/partition_placement.txt")
sftp3.put("ins_folder/files/partition_placement.txt", "ins_folder/files/partition_placement.txt")
sftp4.put("ins_folder/files/partition_placement.txt", "ins_folder/files/partition_placement.txt")

cmd_source = "nohup ins_folder/codes/agent_source.py > ins_folder/results/nohup_source.txt &"
cmd_destination = "nohup ins_folder/codes/agent_destination.py > ins_folder/results/nohup_destination.txt &"
cmd_inference = "nohup ins_folder/codes/agent_inference.py >  ins_folder/results/nohup_inference.txt &"

ssh1.exec_command(cmd_source)
ssh1.exec_command(cmd_destination)

ssh2.exec_command(cmd_source)
ssh2.exec_command(cmd_destination)

ssh3.exec_command(cmd_source)
ssh3.exec_command(cmd_destination)

ssh4.exec_command(cmd_source)
ssh4.exec_command(cmd_destination)

ssh1.exec_command(cmd_inference)
ssh2.exec_command(cmd_inference)
ssh3.exec_command(cmd_inference)
ssh4.exec_command(cmd_inference)




time.sleep(60)
sftp4.get("ins_folder/results/nohup_destination.txt", "results_after/nohup_destination_4.txt")