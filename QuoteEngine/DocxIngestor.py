from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Parses a docx file."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Create a list of quotes from lines in a docx file.

        Arguments:
            path (str) - the path of the docx file
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot parse docx file.')
        quotes = []
        doc = docx.Document(path)
        for paragraph in doc.paragraphs:
            if paragraph.text != "":
                parse = paragraph.text.split('-')
                quote = QuoteModel(parse[0].strip(), parse[1].strip())
                quotes.append(quote)
        return quotes
