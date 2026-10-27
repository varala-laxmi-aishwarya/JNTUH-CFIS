import socket

def encrypt(text, rails):
    fence = [[] for _ in range(rails)]
    rail, direction = 0, 1
    for char in text:
        fence[rail].append(char)
        rail += direction
        if rail == 0 or rail == rails - 1: direction *= -1
    return "".join(["".join(r) for r in fence])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

text = input("Enter plaintext: ")
rails = int(input("Enter rails: "))
ciphertext = encrypt(text, rails)
print("Encrypted:", ciphertext)

client.send(ciphertext.encode())
client.close()
