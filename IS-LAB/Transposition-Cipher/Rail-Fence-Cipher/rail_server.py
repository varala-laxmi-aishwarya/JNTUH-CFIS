import socket

def decrypt(cipher, rails):
    matrix = [['\n' for _ in range(len(cipher))] for _ in range(rails)]
    rail, direction = 0, 1
    for i in range(len(cipher)):
        matrix[rail][i] = '*'
        rail += direction
        if rail == 0 or rail == rails - 1: direction *= -1
    idx = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if matrix[i][j] == '*' and idx < len(cipher):
                matrix[i][j] = cipher[idx]; idx += 1
    res, rail, direction = [], 0, 1
    for i in range(len(cipher)):
        res.append(matrix[rail][i])
        rail += direction
        if rail == 0 or rail == rails - 1: direction *= -1
    return "".join(res)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen(1)

print("server waiting for connection...")
client, address = server.accept()
print("client connected: ", address)

data = client.recv(1024).decode()
print("Received cipher: ", data)

rails = int(input("Enter rails: "))
plaintext = decrypt(data, rails)
print("Decrypted message : ", plaintext)

client.close()
server.close()
