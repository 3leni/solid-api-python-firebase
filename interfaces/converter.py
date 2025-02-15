from abc import ABC, abstractmethod
from io import BytesIO

class Converter(ABC):
    @abstractmethod
    def to_pdf(self, image_file) -> BytesIO:
        pass
