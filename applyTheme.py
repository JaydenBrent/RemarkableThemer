import paramiko

# SSH connection details
hostname = "your_remote_host"
port = 22
username = "your_username"
password = "your_password"

# Paths for moving the file
source_path = "/path/to/subfolder/yourfile.txt"
destination_path = "/path/to/destination/yourfile.txt"

# Create an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the remote server
    ssh.connect(hostname, port=port, username=username, password=password)
    
    # Create an SFTP session
    sftp = ssh.open_sftp()

    # Move the file (equivalent to renaming)
    sftp.rename(source_path, destination_path)

    print(f"File moved from {source_path} to {destination_path}")

    # Close the SFTP session
    sftp.close()
finally:
    # Close the SSH connection
    ssh.close()
