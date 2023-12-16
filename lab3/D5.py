from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Hash import MD5

input_file = "Encrypted5"
with open(input_file, 'rb') as file_in: data = file_in.read()

h = MD5.new()
count, BLOCKSIZE = 0, 64

with open( 'R5.py' , 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        count = count + 1
        h.update(buf)
        buf = afile.read(BLOCKSIZE)

hf = h.digest()

cipher = AES.new(hf, AES.MODE_CBC)
decrypted_data = unpad(cipher.decrypt(data), AES.block_size)

print(decrypted_data.decode('utf-8', errors='ignore'))
