import paramiko
import networkCheck
import netifaces

def remarkableIpFind(username,password):

    # Get the default gateway's IP address
    gateways = netifaces.gateways()
    ip = gateways['default'][netifaces.AF_INET][0]
    
    # Add '/24' to the end of the IP address to form the network range
    network_range = f"{ip}/24"
    
    # Scan the network for SSH
    remarkableIP = networkCheck.scan_network_for_ssh(network_range)
    
    # If the first scan fails, prompt the user for manual input
    while not remarkableIP:
        network_range = input("Please enter the network range to scan (e.g., 192.168.1.0/24): ")
        remarkableIP = networkCheck.scan_network_for_ssh(network_range)
    
    # Try to connect via SSH
    while True:
        try:
            # Attempt the SSH connection
            ssh_test(remarkableIP,username,password)
            print(f"Successfully connected to {remarkableIP}")
            break  # Exit the loop if the connection is successful
        
        except paramiko.AuthenticationException:
            print("Authentication failed, please verify your credentials.")
            break
        
        except paramiko.SSHException as e:
            print(f"SSH connection error: {e}")
            break
        
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    return remarkableIP  # Return the IP when successful or after failure

def ssh_test(ip, username, password):
    # Create an SSH client instance
    ssh_client = paramiko.SSHClient()
    
    # Automatically add the server's host key (for simplicity, consider security implications)
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Connect to the SSH server
        ssh_client.connect(ip, username=username, password=password)
        
        print(f"Connected to {ip}")
        
        # Execute a command on the server (optional)
        stdin, stdout, stderr = ssh_client.exec_command('ls /usr/share/remarkable/')
        # Print the command output
        #print("Command output:")
        #print(stdout.read().decode())


        
    except paramiko.AuthenticationException:
        print("Authentication failed, please verify your credentials")
    except paramiko.SSHException as e:
        print(f"Unable to connect to {ip}: {e}")
    finally:
        # Close the SSH connection
        ssh_client.close()

def backupOriginalPhotos(ip, username, password):

    print("running backupOriginal")

    # Create an SSH client instance
    ssh_client = paramiko.SSHClient()
    
    # Automatically add the server's host key (for simplicity, consider security implications)
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Connect to the SSH server
        ssh_client.connect(ip, username=username, password=password)
        
        print(f"Connected to {ip}")
        
        # First, create the original directory if it doesn't exist
        mkdir_command = 'mkdir -p /usr/share/remarkable/original'
        stdin, stdout, stderr = ssh_client.exec_command(mkdir_command)
        
        # Check for errors in the mkdir command
        stderr_output = stderr.read().decode()
        if stderr_output:
            print("Error creating directory:")
            print(stderr_output)
        else:
            print("Directory created or already exists.")
        
        # Now, execute the command to copy .png files
        copy_command = 'cp /usr/share/remarkable/*.png /usr/share/remarkable/original/'
        stdin, stdout, stderr = ssh_client.exec_command(copy_command)
        
        # Read and print the command output
        stdout_output = stdout.read().decode()
        stderr_output = stderr.read().decode()

        if stdout_output:
            print("Copy command output:")
            print(stdout_output)
        
        if stderr_output:
            print("Command errors:")
            print(stderr_output)

    except paramiko.SSHException as e:
        print(f"SSH connection failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the SSH connection
        ssh_client.close()
        print(f"SSH connection to {ip} closed.")


if __name__ == "__main__":
    ip = "192.168.1.14"  # Replace with the IP address of the SSH server
    username = "root"  # Replace with your SSH username
    password = "7Qu5AbYMdl"  # Replace with your SSH password
    
    ssh_test(ip, username, password)
