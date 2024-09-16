import remarkableTools
import themefinder
import menu

ip = ""
program = True
username = "root"  # Replace with your SSH username
password = "7Qu5AbYMdl"  # Replace with your SSH password


while (program):

    #remarkableTools.backupOriginalPhotos(ip,username,password)
    choice = menu.main_menu(["Connect", "Backup Photos", "Pick Theme","Exit"] )
    print(f"You've got {choice} through to the main program")
    if choice == "Connect":
        if ip == "":
            ip = remarkableTools.remarkableIpFind(username,password)
            connect = menu.main_menu(["Connected"])
        
        remarkableTools.ssh_test(ip,username,password)
    elif choice == "Backup Photos":
        if ip == "":
            ip = remarkableTools.remarkableIpFind(username,password)
        
        remarkableTools.backupOriginalPhotos(ip,username,password)
    elif choice == "Pick Theme":

        if ip == "":
            ip = remarkableTools.remarkableIpFind(username,password)
            connect = menu.main_menu(["Connected"])
        theme = themefinder.themePicker()
        apply = menu.main_menu(["Accept", "Decline"] )
        if apply == "Accept":
            themefinder.applyTheme(ip,username,password,theme)
            menu.main_menu(["Theme Applied"])
    elif choice == "Exit":
        program = False






