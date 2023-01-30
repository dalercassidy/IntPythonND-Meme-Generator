from typing import List
import os.path
from .QuoteModel import QuoteModel
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .TextIngestor import TextIngestor
from .PDFIngestor import PDFIngestor
from .IngestorInterface import IngestorInterface


class Ingestor(IngestorInterface):
    """Strategy Object for parsing files."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Choose the correct strategy to parse quotes.

        Arguments:
            path (str) - the path of the file.
        """
        if not os.path.isfile(path):
            raise Exception(f'{path} cannot be found')
        ext = path.split('.')[-1]
        if ext == "csv":
            quotes = CSVIngestor.parse(path)
        elif ext == "docx":
            quotes = DocxIngestor.parse(path)
        elif ext == "pdf":
            quotes = PDFIngestor.parse(path)
        elif ext == "txt":
            quotes = TextIngestor.parse(path)
        else:
            raise Exception(f'Invalid extension: {ext}')
        return quotes
