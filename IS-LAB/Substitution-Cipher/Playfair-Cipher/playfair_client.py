import socket

def prepare_text(text):
    text = "".join([c.upper() for c in text if c.isalpha()]).replace("J", "I")
    i = 0
    while i < len(text) - 1:
        if text[i] == text[i + 1]:
            text = text[:i + 1] + "X" + text[i + 1:]
        i += 2
    if len(text) % 2 != 0: text += "X"
    return text

def generate_table(key):
    key = "".join(dict.fromkeys([c.upper() for c in key if c.isalpha()]).keys()).replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    table_chars = key + "".join([c for c in alphabet if c not in key])
    return [list(table_chars[i:i+5]) for i in range(0, 25, 5)]

def find_pos(table, char):
    for r, row in enumerate(table):
        if char in row: return r, row.index(char)

def playfair_encrypt(text, key):
    table = generate_table(key)
    text = prepare_text(text)
    cipher = ""
    for i in range(0, len(text), 2):
        r1, c1 = find_pos(table, text[i])
        r2, c2 = find_pos(table, text[i+1])
        if r1 == r2: cipher += table[r1][(c1 + 1) % 5] + table[r2][(c2 + 1) % 5]
        elif c1 == c2: cipher += table[(r1 + 1) % 5][c1] + table[(r2 + 1) % 5][c2]
        else: cipher += table[r1][c2] + table[r2][c1]
    return cipher

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

text = input("Enter plaintext: ")
key = input("Enter secret key: ")
ciphertext = playfair_encrypt(text, key)

print("Encrypted Text:", ciphertext)
client.send(ciphertext.encode())

client.close()
