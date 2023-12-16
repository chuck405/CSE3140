import os, secrets
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

k = secrets.token_bytes(32)
pem_public_key = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3i2sT28SuRCZPyEjZMxA
hei3OsoqISWHoQgqUz3gZSEtk1t2t/knVXv+6wwdJ65zPo80BiwDzOS9kNzUtREU
+FpMMls6TZfNhBFbpWfCWDhQgFknNPK8iL9VqaD0tf6v4BjxRTREbqKss2HAlN1l
OYM5gdQv6dWaappliMBy62Xc9i4wUHi7QssDZnLPL3pNwqvTJZCgSDX8Tmb5qqx1
7z4p+i9mX5Z6eCvuOkwvIFQ2bm2Fjv3toTWeZ8P+LnCJcIP/1/PLnP0OoaTGpJP2
eui+tQmuEGjU1LEYLAxBY3gw9mk65IRoBFz5BOvvxKn3w1YK4BfghDaC/VVwT9jV
MQIDAQAB
-----END PUBLIC KEY-----
"""

public_key = serialization.load_pem_public_key(pem_public_key.encode(), backend=default_backend())
encrypted_shared_key = public_key.encrypt(k, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
with open("EncryptedSharedKey", "wb") as file: file.write(encrypted_shared_key)

folder_path = "/home/cse/Lab3/Q6files/"
txt_files = [file for file in os.listdir(folder_path) if file.endswith(".txt")]

for file in txt_files:
    file_path = os.path.join(folder_path, file)
    with open(file_path, "rb") as file: 
        data = file.read()
        cipher = AES.new(k, AES.MODE_CBC)
        ciphered_data = cipher.encrypt(pad((data), AES.block_size))
    with open(file_path + ".encrypted", "wb") as output_file: 
        output_file.write(ciphered_data)
