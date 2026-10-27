import socket

def encrypt(text, key):
    clean_text = text.replace(" ", "")
    plain_len = len(clean_text)
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    cols = len(key)
    rows = -(-plain_len // cols)
    padded_text = clean_text.ljust(rows * cols, 'X')
    matrix = [list(padded_text[i:i+cols]) for i in range(0, len(padded_text), cols)]
    ciphertext = "".join(["".join(matrix[r][i] for r in range(rows)) for i, _ in key_order])
    return plain_len, ciphertext

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

text = input("Enter plaintext: ")
key = input("Enter keyword: ")
length, ciphertext = encrypt(text, key)
print("Encrypted:", ciphertext)

# Send length and ciphertext together
client.send(f"{length}:{ciphertext}".encode())
client.close()
