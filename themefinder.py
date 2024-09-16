import os
import menu
import paramiko


#print ("Testing dir list:")
#print(os.listdir("Themes"))

def ListThemes():
    themes = os.listdir("Themes")

    return themes

def themePicker():

    options = ListThemes()
    print (options)
    choice = menu.main_menu(options)

    return choice

def applyTheme(ip,username,password,theme):
    

    # Paths for moving the file
    source_path = f"Themes/{theme}/suspended.png"
    print (source_path)
    destination_path = "/usr/share/remarkable/suspended.png"

    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the remote server
        ssh.connect(ip, "22", username, password)
    
        # Create an SFTP session
        sftp = ssh.open_sftp()
        sftp.put(source_path, destination_path)

        print(f"File moved from {source_path} to {destination_path}")

        # Close the SFTP session
        sftp.close()
    finally:
    # Close the SSH connection
        ssh.close()

#themePicker()