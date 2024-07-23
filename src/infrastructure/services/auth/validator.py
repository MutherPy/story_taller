from configs.main_config import Secrets
from cryptography.fernet import Fernet


class PasswordsService:

    @staticmethod
    def validate_password(password: str, storing_password: str) -> bool:
        decr_pass = PasswordsService._decrypt_password(storing_password)
        return decr_pass == password

    @staticmethod
    def encrypt_password(password: str) -> str:
        fernet = Fernet(Secrets.passwords_secret)
        return fernet.encrypt(password.encode('utf-8')).decode('utf-8')

    @staticmethod
    def _decrypt_password(ecr_password: str) -> str:
        fernet = Fernet(Secrets.passwords_secret)
        return fernet.decrypt(ecr_password.encode('utf-8')).decode('utf-8')

