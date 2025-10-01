# HELLO 
# Shift 3
# KHOOR
def caesar_encrypt(text, shift=1):
    result = ""
    for char in text:
        if char.isupper():
            position = ord(char) - ord('A')
            new_position = (position + shift) % 26
            new_char = chr(new_position + ord('A'))
            result += new_char
        elif char.islower():
            position = ord(char) - ord('a')
            new_position = (position + shift) % 26
            new_char = chr(new_position + ord('a'))
            result += new_char
        else:
            result += char

    return result

print(caesar_encrypt("hello"))
print(caesar_encrypt("hello", 4))


def caesar_decrypt(text, shift):
    pass