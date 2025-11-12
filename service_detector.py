import socket
def advanced_service_detector(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((target, port))

        if port in [80, 443, 8080]:
            sock.send(b'GET / HTTP/1.1\r\nHost: target\r\n\r\n')
        response = sock.recv(4096).decode('utf-8', errors='ignore')
        sock.close()
        if 'Apache' in response:
            return 'Apache web server'
        elif 'nginx' in response:
            return 'Nginx web server'
        elif 'Microsoft-IIS' in response:
            return 'IIS Web Server'
        else:
            return response[:100]
    except Exception as e:
        print("error", e)

print(advanced_service_detector('45.33.32.156', 80))