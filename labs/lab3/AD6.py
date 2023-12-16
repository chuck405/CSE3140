from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

with open("EncryptedSharedKey", "rb") as encrypted_shared_key_file: encrypted_shared_key = encrypted_shared_key_file.read()

pem_private_key = """
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDeLaxPbxK5EJk/
ISNkzECF6Lc6yiohJYehCCpTPeBlIS2TW3a3+SdVe/7rDB0nrnM+jzQGLAPM5L2Q
3NS1ERT4WkwyWzpNl82EEVulZ8JYOFCAWSc08ryIv1WpoPS1/q/gGPFFNERuoqyz
YcCU3WU5gzmB1C/p1ZpqmmWIwHLrZdz2LjBQeLtCywNmcs8vek3Cq9MlkKBINfxO
ZvmqrHXvPin6L2Zflnp4K+46TC8gVDZubYWO/e2hNZ5nw/4ucIlwg//X88uc/Q6h
pMakk/Z66L61Ca4QaNTUsRgsDEFjeDD2aTrkhGgEXPkE6+/EqffDVgrgF+CENoL9
VXBP2NUxAgMBAAECggEAAlsro6AC69GAPookbPI5kPH513bDYZybRprmkAFs+sWS
TSjAJo1O3Ho3Jtj3Ci+way5rl9EprSeT1xBwdQccWNHkUvhisuX0OP1SInvqNLNM
L0BCyS31z+FvkB/z2GY+CTtae6hlPWMeP7y+pRV/+E8q8fSFGY65V34Rq5SW42Yp
FYq78sSgDAeZuvqxQV87TD9hwPWz+TXxh6ZVVYeiQV7LtX+04StpgNfDAyloGo1/
Cp8KO+7o+5EZ/etH52NKoyypHel1skiX5MQ5XPsnChkqsw2B8rogyKKOzbow3XMp
UH+WYpw8/N7Rogh95Doje/6DvzGxaW3j5w4w9ocmkQKBgQDzLibPfsiaUFs6f78N
MoMOgaOnl08e5yR0rkcz1AO5Hdug/B4bJ7o5/cuNvIDAEtJVfgivKaVqkHWlhZCh
MkXdaza6PxgZh3BLx7WJAUEXKPwizArqy+kw5thfVR5oJPdcwScJ0KI+6dvMEKCd
RQh1HW0iz5tcP1/3LVw95ty2ZQKBgQDp5BcJVhTBTeqIOiksao2nUbm2S8kUv8OJ
P6sDZw/0EXVKojJONelDswEHYUcZnJKairNZKxgVH3PjJMVLDuFcp6HiTSKP7DA9
vwCBVoSXZnnCgWnzbzLWHIAoV9obrbvZ28lq1cWT4jgOzfC8r4EzxfTJ96UuB/Mn
pHlf0evg3QKBgHgciYrfQlIF8ql4Q3NPSbA2lBDJCYln/XesRPryc0xR1RM0s+IR
w0e1dX7yZl14bm9PqxZpaYyzAYjZ6c/UtvFgbU2csFibrvmfEKk092NrGO5O/e1u
/iTrQGAF+NjTuWIU/SU56YlNlQS8CbjkSgMen7Mb+86adtnti6v/hXCJAoGBAKkK
pvOieWG0dJt8naFyaWrSkEyGvY/3gNVDZNASvt8Bdyo3y+/m2u6JA2dYEVEbboGv
WSxLDx7FGrbCLq2u1YZnyYKLiT1H0R3vW+gepbne4IWJjw/YAH/rHV0LEaILkMdG
KG7EjgXx694XTbSxi8nleqQ2DfYU3NJ79xUf3UEpAoGAPjEWzOy9WqgMDqQaV8N8
2Hqzd+k9nxFH5n26nVtQakGNYi5+jqpvtHqKn+JoEp1MBa7LauTJlF3JKP8QiYML
gIfyq57u7ZkOtrfyAmtjz1JRmnZvzpZjD3SczfML1Z+GCMNZ7+lhSltyrmrOKVFY
R/Wyt/FSXHaFaWlqiAWSOWo=
-----END PRIVATE KEY-----
"""
private_key = serialization.load_pem_private_key(pem_private_key.encode(), password=None, backend=default_backend())

k = private_key.decrypt(encrypted_shared_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
with open("DecryptedSharedKey", "wb") as decrypted_shared_key_file: decrypted_shared_key_file.write(k)
