import base64
from cryptography.fernet import Fernet

class EncryptionKeyException(Exception):
    pass

def encrypt_aes(key: str, data: str) -> str:
    """Encrypt the data using Fernet encryption and return as base64 encoded string."""
    try:
        fernet = Fernet(key.encode("utf-8"))
        return fernet.encrypt(data.encode("utf-8")).decode("utf-8")
    except ValueError:
        raise EncryptionKeyException("Invalid secret key")

def decrypt_aes(key: str, encoded_data: str) -> str:
    """Decrypt the encrypted data using Fernet decryption."""
    try:
        fernet = Fernet(key.encode("utf-8"))
        return fernet.decrypt(encoded_data.encode("utf-8")).decode("utf-8")
    except ValueError:
        raise EncryptionKeyException("Invalid secret key")

TOKEN_TO_BE_DECRYPTED = input("enter the encrypted password:")
SECRET_KEY = input("Enter the the secret key:")

decrypted_token = decrypt_aes(SECRET_KEY, TOKEN_TO_BE_DECRYPTED)
print("Decrypted Token:", decrypted_token)
