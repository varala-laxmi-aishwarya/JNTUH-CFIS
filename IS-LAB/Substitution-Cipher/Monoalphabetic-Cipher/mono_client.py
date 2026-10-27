import socket

def encrypt_monoalphabetic(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()
    result = ""

    # Create a mapping from original alphabet letter to key letter
    alpha_to_key = {a: k for a, k in zip(alphabet, key)}

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            cipher_char = alpha_to_key.get(char.upper(), char)
            result += cipher_char if is_upper else cipher_char.lower()
        else:
            result += char
    return result

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5001))

text = input("Enter plaintext: ")
key = input("Enter secret key (26 letters): ").strip()

if len(key) == 26 and key.isalpha():
    ciphertext = encrypt_monoalphabetic(text, key)
    print("Encrypted:", ciphertext)
    client.send(ciphertext.encode())
else:
    print("Invalid key! Must be exactly 26 letters.")

client.close()