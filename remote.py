import boto3
import paramiko

# EC2 instance details
instance_id1 = 'i-08c9e99022a077e2e'
instance_id2 = 'i-0ad735898c7080c7b'

# SSH key pair details
key_name = 'rdpkeypair'
private_key_path = r'C:\Users\sterl\Downloads\rdp-keypair.pem'

# Connect to EC2 instances
ec2 = boto3.resource('ec2')

instance1 = ec2.Instance(instance_id1)
instance2 = ec2.Instance(instance_id2)

# Get public IP addresses
ip_address1 = instance1.public_ip_address
ip_address2 = instance2.public_ip_address

# Establish SSH connection to instance 1
ssh_client1 = paramiko.SSHClient()
ssh_client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client1.connect(ip_address1, username='ec2-user', key_filename=private_key_path)

# Establish SSH connection to instance 2
ssh_client2 = paramiko.SSHClient()
ssh_client2.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client2.connect(ip_address2, username='ec2-user', key_filename=private_key_path)

# Execute remote commands on instance 1
stdin, stdout, stderr = ssh_client1.exec_command('ls')  # List files in the current directory
print(stdout.read().decode())

stdin, stdout, stderr = ssh_client1.exec_command('pwd')  # Print the current working directory
print(stdout.read().decode())

stdin, stdout, stderr = ssh_client1.exec_command('echo "Hello, Instance 1"')  # Echo a message
print(stdout.read().decode())

stdin, stdout, stderr = ssh_client1.exec_command('whoami')  # Get the username of the current user
print(stdout.read().decode())

stdin, stdout, stderr = ssh_client1.exec_command('df -h')  # Check disk usage
print(stdout.read().decode())

stdin, stdout, stderr = ssh_client1.exec_command('ps aux')  # List running processes
print(stdout.read().decode())

# Execute remote commands on instance 2
stdin, stdout, stderr = ssh_client2.exec_command('ls')  # List files in the current directory
print(stdout.read().decode())

stdin, stdout, stderr = ssh_client2.exec_command('pwd')  # Print the current working directory
print(stdout.read().decode())

stdin, stdout, stderr = ssh_client2.exec_command('echo "Hello, Instance 2"')  # Echo a message
print(stdout.read().decode())

stdin, stdout, stderr = ssh_client2.exec_command('uname -a')  # Get the system information
print(stdout.read().decode())

stdin, stdout, stderr = ssh_client2.exec_command('free -m')  # Check memory usage
print(stdout.read().decode())

stdin, stdout, stderr = ssh_client2.exec_command('netstat -tuln')  # List open network ports
print(stdout.read().decode())

# Close SSH connections
ssh_client1.close()
ssh_client2.close()
