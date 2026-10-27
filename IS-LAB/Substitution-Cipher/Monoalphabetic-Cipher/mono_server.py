import socket

def decrypt_monoalphabetic(cipher_text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()
    result = ""

    # Create a mapping from key letter back to original alphabet letter
    key_to_alpha = {k: a for k, a in zip(key, alphabet)}

    for char in cipher_text:
        if char.isalpha():
            is_upper = char.isupper()
            original_char = key_to_alpha.get(char.upper(), char)
            result += original_char if is_upper else original_char.lower()
        else:
            result += char
    return result

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5001))
server.listen(1)

print("Server waiting for connection...")
client, address = server.accept()
print("Client connected:", address)

data = client.recv(1024).decode()
print("Received cipher:", data)

key = input("Enter the secret key (26 letters): ").strip()
if len(key) == 26 and key.isalpha():
    plaintext = decrypt_monoalphabetic(data, key)
    print("Decrypted message:", plaintext)
else:
    print("Invalid key length. Must be 26 unique alphabetic characters.")

client.close()
server.close()