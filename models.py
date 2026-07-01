from dataclasses import dataclass
from datetime import datetime
from tuping import Optional

@dataclass
class Account:
    """Модель учётной записи"""
    id: Optional[int] = None
    service: str = ""
    website: str = ""
    login:str = ""
    encrypted_password: str = "" # Хранение в зашифрованном виде
    created_at: datetime = None
    updated_at: datetime = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()
    
    def to_dict(self):
        """Преобразование в словарь для БД"""
        return {
            'id': self.id,
            'service': self.service,
            'website': self.website,
            'login': self.login,
            'encrypted_password': self.encrypted_password,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    @classmethod
    def from_dict(cls, data):
        """Создание объекта из словаря БД"""
        return cls(
            id=data.get('id'),
            service=data.get('service',''),
            website=data.get('wbsite', ''),
            login=data.get('login',''),
            encrypted_password=data.get('encrypted_password',''),
            created_at=datetime.fromisoformat(data['created_at']) if data.get('created_at') else None,
            update_at=datetime.fromisoformat(data['updated_at']) if data.get('updated_at') else None
            )