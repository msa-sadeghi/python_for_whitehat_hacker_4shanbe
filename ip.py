
# کلاس A: 1.0.0.0 تا 126.255.255.255 (شبکه‌های بزرگ)
# کلاس B: 128.0.0.0 تا 191.255.255.255 (شبکه‌های متوسط)
# کلاس C: 192.0.0.0 تا 223.255.255.255 (شبکه‌های کوچک)
# کلاس D: 224.0.0.0 تا 239.255.255.255 (Multicast)
# کلاس E: 240.0.0.0 تا 255.255.255.255 (تجربی)


# 127.0.0.1: localhost (خود سیستم)
# 0.0.0.0: همه آدرس‌ها
# 255.255.255.255: broadcast

# import re
# def validate_ipv4_simple(ip):
#     pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3}).(\d{1,3})$'
#     res = re.match(pattern, ip)

#     if not res:
#         return False
#     for octet in res.groups():
#         if int(octet) > 255:
#             return False
#     return True

# print(validate_ipv4_simple("300.168.1.1"))
# print(validate_ipv4_simple("127.168.1.1"))

# import ipaddress

# def validate_ip(ip):
#     try:
#         ip = ipaddress.ip_address(ip)
#         return True,  ip
#     except ValueError as e:
#         return False, str(e)
    
# print(validate_ip("123.56.87.45"))



import ipaddress
import socket


class IPAnalyzer:
    def __init__(self, ip_string):
        try:
            self.ip = ipaddress.ip_address(ip_string)
            self.is_valid = True
        except ValueError:
            self.is_valid = False
            self.ip = None

    def get_version(self):
        if not self.is_valid:
            return None
        return self.ip.version
    
    def is_private(self):
        if not self.is_valid:
            return None
        return self.ip.is_private
    def is_loopback(self):
        if not self.is_valid:
            return None
        return self.ip.is_loopback
    def get_class(self):
        if not self.is_valid or self.ip.version != 4:
            return None
        first_octet = int(str(self.ip).split('.')[0])
        if 1 <= first_octet <= 126:
            return 'A'
        elif 128 <= first_octet <= 191:
            return 'B'
        elif 192 <= first_octet <= 223:
            return 'C'
        elif 224 <= first_octet <= 239:
            return 'D'
        else:
            return 'E'
    

    

ip_an = IPAnalyzer("192.168.1.1")
print(ip_an.get_class())
print(ip_an.get_version())
print(ip_an.is_private())
print(ip_an.is_loopback())
