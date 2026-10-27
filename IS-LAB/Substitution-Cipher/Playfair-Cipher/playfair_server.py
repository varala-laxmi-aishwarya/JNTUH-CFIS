import socket

def generate_table(key):
    key = "".join(dict.fromkeys([c.upper() for c in key if c.isalpha()]).keys()).replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    table_chars = key + "".join([c for c in alphabet if c not in key])
    return [list(table_chars[i:i+5]) for i in range(0, 25, 5)]

def find_pos(table, char):
    for r, row in enumerate(table):
        if char in row: return r, row.index(char)

def playfair_decrypt(ciphertext, key):
    table = generate_table(key)
    plain = ""
    for i in range(0, len(ciphertext), 2):
        r1, c1 = find_pos(table, ciphertext[i])
        r2, c2 = find_pos(table, ciphertext[i+1])
        if r1 == r2: plain += table[r1][(c1 - 1) % 5] + table[r2][(c2 - 1) % 5]
        elif c1 == c2: plain += table[(r1 - 1) % 5][c1] + table[(r2 - 1) % 5][c2]
        else: plain += table[r1][c2] + table[r2][c1]
    return plain

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen(1)

print("server waiting for connection...")
client, address = server.accept()
print("client connected: ", address)

data = client.recv(1024).decode()
print("Received cipher: ", data)

key = input("Enter secret key: ")
print("Decrypted:", playfair_decrypt(data, key))

client.close()
server.close()
