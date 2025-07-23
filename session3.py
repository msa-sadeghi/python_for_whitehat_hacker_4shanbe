import socket

site_name = input("enter site's name: ")
try:
    ip = socket.gethostbyname(site_name)
    print(f"{site_name} is is : {ip}")
except:
    print("error")


def is_private_ip(ip):
    parts = list(map(int,ip.split('.')))
    print(parts)
    if parts[0] == 10:
        return True
    if parts[0] == 172 and 16 <= parts[1] <= 31:
        return True
    if parts[0] == 192 and parts[1] == 168:
        return True
    return False



print(is_private_ip(ip))