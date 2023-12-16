from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def generate_private_key():
    return rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())

private_key = generate_private_key()
public_key = private_key.public_key()

public_key_pem = public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)
private_key_pem = private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption())

with open("e.key", "wb") as public_key_file: public_key_file.write(public_key_pem)
with open("d.key", "wb") as private_key_file: private_key_file.write(private_key_pem)
