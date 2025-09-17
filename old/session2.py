# from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# key = b'jJzer4MHK8dKkMC1ZFLy9XgQ7UmQQtJKN41XFK5XNFk='

# c = Fernet(key)
# password = "sara"
# hashed_password = c.encrypt(password.encode())
# print(hashed_password)
# x = b'gAAAAABod57XQYh9SPbcoehCVhFZtaEuK1hmcdomrfSzdj8htH97Oho7PyPy6mX51ubyrUtZae99hst2oRX6gtDbuDoXiRaiwg=='
# print(c.decrypt(x))

import requests
import hashlib

password = "Artin@1234#"
sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
prefix = sha1[:5]
res = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
if sha1[5:] in res.text:
    print("your password is pwned")
else:
    print("your password not pwned")