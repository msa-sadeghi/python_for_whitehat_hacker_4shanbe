# from cryptography.fernet import Fernet
# key  = Fernet.generate_key()
# cipher = Fernet(key)

# message = "this is s secret message"
# encrypted = cipher.encrypt(message.encode())

# print(f"original message: {message}")
# print(f"encrypted message: {encrypted}")

# decrypted = cipher.decrypt(encrypted)
# print(f"dercypted message is :{decrypted.decode()}")

from cryptography.fernet import Fernet
import os

def generate_key(filename='secret.key'):
    key = Fernet.generate_key()
    with open(filename, 'wb') as key_file:
        key_file.write(key)

    return key

def load_key(filename='secret.key'):
    with open(filename, 'rb') as key_file:
        return key_file.read()


def encrypt_file(filename, key):
    cipher = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()

    encrypted_data = cipher.encrypt(file_data)
    with open(filename, 'wb') as file:
        file.write(encrypted_data)
    print(f"file {filename} encrypted")

def decrypt_file(filename, key):
    pass