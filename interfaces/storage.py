from abc import ABC, abstractmethod
from io import BytesIO

class Storage(ABC):
    @abstractmethod
    def upload(self, file_bytes: BytesIO, filename: str) -> str:
        pass
    
    @abstractmethod
    def save_user(self, user_data: dict) -> None:
        pass
