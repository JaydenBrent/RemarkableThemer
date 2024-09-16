import nmap

def scan_network_for_ssh(range_ip):
    nm = nmap.PortScanner()
    nm.scan(hosts=range_ip, arguments='-p 22 --open -sV')
    
    matching_ip = ""
    
    for host in nm.all_hosts():
        if 'tcp' in nm[host] and 22 in nm[host]['tcp']:
            service = nm[host]['tcp'][22]['product']
            version = nm[host]['tcp'][22]['version']
            
            if 'Dropbear' in service and version == '2020.81':
                matching_ip = host
                print (matching_ip)
                
    
    return matching_ip


