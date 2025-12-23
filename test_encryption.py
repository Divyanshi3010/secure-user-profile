from utils.encryption import encrypt, decrypt
from config import Config

def test_encrypt_decrypt():
    text = "123412341234"
    encrypted = encrypt(text, Config.AES_SECRET_KEY)
    decrypted = decrypt(encrypted, Config.AES_SECRET_KEY)
    assert decrypted == text
