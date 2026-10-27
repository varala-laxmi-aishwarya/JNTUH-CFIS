import socket

def encrypt_caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

text = input("Enter plaintext: ")
shift = int(input("Enter secret key: "))
ciphertext = encrypt_caesar(text, shift)
print("Encrypted: ", ciphertext)

client.send(ciphertext.encode())
client.close()
