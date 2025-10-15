import socket
import threading
from datetime import datetime
from queue import Queue

class PortScanner:
    COMMON_PORTS = {
        21:"FTP",
        22:"SSH",
        23:"telnet"
    }

    def __init__(self, target, timeout=1, num_threads = 100):
        """
            initialization
            Args:
                target (str): IP or hostname
                timeout (float): timeout
                num_threads (int): threads
        """
        self.target = target
        self.timeout= timeout
        self.num_threads = num_threads
        self.open_ports = []

    def scan(self, start_port = 1, end_port = 1024):
        queue = Queue()

        threads = []
        for i in range(self.num_threads):
            thread = threading.Thread(target=self.worker, args=(queue,))
            thread.daemon = True
            thread.start()
            threads.append(thread)
        for port in range(start_port, end_port + 1):
            queue.put(port)
        queue.join()

        ## TODO stop thread

        
    def worker(self, queue):
        while True:
            port = queue.get()
            if port is None:
                break
            self.scan_port(port)
            queue.task_done()

    def scan_port(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.target, port))
            if result == 0:
                try:
                    sock.send(b'Hello')
                    banner = sock.recv(1024).decode().stript() 
                except:
                    banner = ""
                service = self.COMMON_PORTS[port]
                self.open_ports.append(
                    {
                        'port':port,
                        'service': service,
                        'banner' :  banner
                    }
                )
                print(f"port {port}  | {service} | {banner}")

            sock.close()
        except Exception as e:
            pass







