from scapy.all import IP, TCP, sr1, conf

conf.verb = 0

def syn_scan(target, port):
    syn_packet = IP(dst=target)/TCP(dport=port, flags='S')
    response = sr1(syn_packet, timeout=1)
    if response and response.haslayer(TCP):
        if response[TCP].flags == 0x12:
            rst_packet = IP(dst=target)/TCP(dport=port, flags='R')
            sr1(rst_packet, timeout=1)
            return True
    return False
if syn_scan('45.33.32.156', 80) == True:
    print("port number 80 is open")