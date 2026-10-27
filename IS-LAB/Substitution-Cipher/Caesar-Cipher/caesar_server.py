import socket

def decrypt_caesar(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen(1)

print("server waiting for connection...")
client, address = server.accept()
print("client connected: ", address)

data = client.recv(1024).decode()
print("Received cipher: ", data)

shift = int(input("Enter the secert key: "))
plaintext = decrypt_caesar(data, shift)
print("Decrypted message : ", plaintext)

client.close()
server.close()
