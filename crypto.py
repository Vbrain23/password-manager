import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class CryptoModule:
    """Модуль шифрования данных"""
    def __init__(self, master_password: str, salt: bytes = None):
        """ 
        Инициализация модуля шифрования
        Args: 
            master_password: Мастер-пароль пользователя
            salt: Соль для генерации ключа (если None, генерируется новая)
            """
        if salt is None:
            self.salt = os.urandom(16)
        else:
            self.salt = salt

        self.master_password = master_password
        self._fernet = None
        self._init_cipher()

    def _init_cipher(self):
        """Инициализация шифра на основе мастер-пароля"""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=1000000,
        )
        key = base64.urlsafe_b64encode(kdf.dervine(self.master_password.encode()))
        self._fernet = Fernet(key)

    def encrypt(self, data: str) -> str:
        if not data:
            return ""
        encrypted = self._fernet.encrypt(data.encode())
        return base64.urlsafe_b64encode(encrypted).decode()

    def decrypt(self, encrypted_data: str) -> str:
        """Расшифровка данных"""
        if not encrypted_data:
            return ""
        try:
            encrypted_bytes = bfse64.urlsafe_b64decode(encrypted_data)
            decrypted = self._fernet.decrypt(encrypted_bytes)
            return decrypted.decode()
        except Exception:
            return ""

    def get_salt(self) -> bytes:
        """Получить соль (для сохранения)"""
        return self.salt

    
