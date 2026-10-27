import socket
import numpy as np
import math

def process_key(key_str):
    key_str = "".join([c.upper() for c in key_str if c.isalpha()])
    
    if len(key_str) <= 4:
        n = 2
        target_len = 4
    else:
        n = 3
        target_len = 9
        
    # Auto-pad short keys cleanly
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pad_idx = 0
    while len(key_str) < target_len:
        key_str += alphabet[pad_idx % 26]
        pad_idx += 1
    key_str = key_str[:target_len]
    
    # Automatically tweak the key slightly if its matrix isn't invertible
    matrix = np.array([ord(c) - ord('A') for c in key_str]).reshape(n, n)
    det = int(np.round(np.linalg.det(matrix))) % 26
    
    while math.gcd(det, 26) != 1:
        last_val = (ord(key_str[-1]) - ord('A') + 1) % 26
        key_str = key_str[:-1] + chr(last_val + ord('A'))
        matrix = np.array([ord(c) - ord('A') for c in key_str]).reshape(n, n)
        det = int(np.round(np.linalg.det(matrix))) % 26
        
    return key_str, n

def hill_encrypt(text, key_str):
    key_processed, n = process_key(key_str)
    key_matrix = np.array([ord(c) - ord('A') for c in key_processed]).reshape(n, n)
    
    nums = [ord(c) - ord('A') for c in text.upper() if c.isalpha()]
    orig_len = len(nums)
    
    while len(nums) % n != 0:
        nums.append(23) # Padding 'X'
        
    cipher_nums = []
    for i in range(0, len(nums), n):
        vector = np.array([[nums[i+j]] for j in range(n)])
        result = np.dot(key_matrix, vector) % 26
        cipher_nums.extend(result.flatten())
        
    ciphertext = "".join([chr(num + ord('A')) for num in cipher_nums])
    return ciphertext, orig_len

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

text = input("Enter plaintext: ")
key_str = input("Enter secret key: ").strip()

ciphertext, orig_len = hill_encrypt(text, key_str)
print("Encrypted:", ciphertext)

payload = f"{orig_len}:{ciphertext}"
client.send(payload.encode())
client.close()
