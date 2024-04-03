from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64
import os

password = input("Enter your password: ")

def encrypt_password(password, key):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

def generate_fernet_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # Length of the derived key
        salt=salt,
        iterations=100000,  # Number of iterations (adjust as needed for security)
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

# Generate a random salt value
salt = os.urandom(16)

fernet_key = generate_fernet_key(password, salt)
print("Generated Fernet Key:", fernet_key)

encrypted_password = encrypt_password(password, fernet_key)
print("Encrypted Password:", encrypted_password)
