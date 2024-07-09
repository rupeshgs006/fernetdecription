import base64
from cryptography.fernet import Fernet

fernet = Fernet(secret_key.encode())
        decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
        return decrypted_password

TOKEN_TO_BE_DECRYPTED = input("enter the encrypted password:")
SECRET_KEY = input("Enter the the secret key:")

decrypted_token = decrypt_aes(SECRET_KEY, TOKEN_TO_BE_DECRYPTED)
print("Decrypted Token:", decrypted_token)
