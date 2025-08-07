import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def aes_ecb_encrypt(plain_bytes: bytes, aes_key: bytes) -> bytes:
    return AES.new(aes_key, AES.MODE_ECB).encrypt(pad(plain_bytes, AES.block_size))


def encrypt_pwd(password: str) ->str:
    return base64.b64encode(aes_ecb_encrypt(password.encode(), "t8b52yrsoyx66f35".encode())).decode()


if __name__ == "__main__":
    pwd = "1"
    print(encrypt_pwd(pwd))