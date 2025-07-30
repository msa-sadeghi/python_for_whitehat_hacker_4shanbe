import socket

# target = input("enter an ip: ")
# ports = [135, 445, 80]

# for port in ports:
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.settimeout(.5)
#     result = sock.connect_ex((target,port))
#     if result == 0:
#         print(f"port{port} is open!!!")
#     sock.close()


html_content = "<html><head><title>scanning ports</title></head><body>"
html_content += f"<h1>report of or port scanning</h1>"
html_content += "</body></html>"

with open("port_scan_report.html", "w", encoding="utf-8") as f:
    f.write(html_content)