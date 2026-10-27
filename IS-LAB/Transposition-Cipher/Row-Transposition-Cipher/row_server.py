import socket
import math

def decrypt(cipher, key, original_len):
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    cols = len(key)
    rows = math.ceil(len(cipher) / cols)
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    char_idx = 0
    for index, _ in key_order:
        for r in range(rows):
            if char_idx < len(cipher):
                matrix[r][index] = cipher[char_idx]; char_idx += 1
    padded_plaintext = "".join(["".join(row) for row in matrix])
    return padded_plaintext[:original_len]  # Truncate strictly to the original length

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen(1)

print("server waiting for connection...")
client, address = server.accept()
print("client connected: ", address)

data = client.recv(1024).decode()
length_str, ciphertext = data.split(":", 1)
print("Received cipher: ", ciphertext)

key = input("Enter keyword: ")
plaintext = decrypt(ciphertext, key, int(length_str))
print("Decrypted message : ", plaintext)

client.close()
server.close()
