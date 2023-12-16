import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

with open("DecryptedSharedKey", "rb") as decrypted_shared_key_file: k = decrypted_shared_key_file.read()

folder_path = "/home/cse/Lab3/Q6files/"
encrypted_files = [file for file in os.listdir(folder_path) if file.endswith(".encrypted")]

for file in encrypted_files:
    file_path = os.path.join(folder_path, file)
    with open(file_path, "rb") as file:
        data = file.read()
        cipher = AES.new(k, AES.MODE_CBC)
        decrypted_data = unpad(cipher.decrypt(data), AES.block_size)
        with open(file_path[:-10:], "wb") as output_file:
            output_file.write(decrypted_data)
