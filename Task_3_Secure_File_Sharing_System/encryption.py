from Crypto.Cipher import AES
from base64 import b64encode, b64decode

key = b'ThisIsASecretKey'  # 16-byte AES key

def pad(data):
    while len(data) % 16 != 0:
        data += b' '
    return data

def encrypt_file(file_data):
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(file_data)
    encrypted = cipher.encrypt(padded)
    return b64encode(encrypted)

def decrypt_file(encrypted_data):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(b64decode(encrypted_data))
    return decrypted.rstrip(b' ')
