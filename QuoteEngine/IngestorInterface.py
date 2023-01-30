from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract interface for parsing quotes."""

    allowed_extensions = ['pdf', 'txt', 'csv', 'docx']

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Determine if class can ingest file.

        Arguments:
            path (str) - the path of the input file
        """
        ext = path.split('.')[-1]
        return True

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Overide this to parse specific file types.

        Arguments:
            path (str) - the path of the input file
        """
        pass
