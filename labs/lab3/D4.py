from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

input_file = "Encrypted4"
with open(input_file, 'rb') as file_in: data = file_in.read()

variable = b'\xab\x02\xf6\xa9\x0ct\xf8\x93\xe3\xc4\xd3\x80,\xbc\xd0\x07'

cipher = AES.new(variable, AES.MODE_CBC)
decrypted_data = unpad(cipher.decrypt(data), AES.block_size)

print(decrypted_data.decode('utf-8', errors='ignore'))
