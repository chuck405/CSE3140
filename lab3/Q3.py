import os, time, hashlib, sys
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

with open('/home/cse/Lab3/Q3pk.pem', "rb") as publicKeyFile:
    publicKey = publicKeyFile.read()

def verify_signature(key, data, sig_file):
    h = SHA256.new(data)
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    with open(sig_file, "rb") as file: signature = file.read()
    return (signer.verify(h, signature))

file_list = os.listdir('/home/cse/Lab3/Q3files/')
for i in file_list:
    if os.path.splitext(i)[1] == ".exe":
        sig_file = str(i) + ".sign"
        with open(os.path.join('/home/cse/Lab3/Q3files/', i), "rb") as file:
            contents = file.read()
            if verify_signature(publicKey, contents, sig_file): print(i)

def slow_verify_signature(key, data, sig_file):
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    with open(sig_file, "rb") as file: signature = file.read()
    return (signer.verify(data, signature))

with open(os.path.join('/home/cse/Lab3/Q3files/', "unneeded.exe"), "rb") as file:
    contents = file.read()

    start = time.time()
    slow_verify_signature(publicKey, contents, "unneeded.exe.sign")
    print(time.time() - start)

    start = time.time()
    verify_signature(publicKey, contents, "unneeded.exe.sign")
    print(time.time() - start)

    
