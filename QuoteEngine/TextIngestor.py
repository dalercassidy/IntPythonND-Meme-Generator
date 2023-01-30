from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Parses a text file."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Create a list of quotes from lines in a txt file.

        Arguments:
            path (str) - the path of the txt file
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot parse txt file.')

        quotes = []

        with open(path, 'r', encoding="utf-8-sig") as f:
            for line in f:
                formatted_line = line.strip(' \n')
                if len(line):
                    words = line.split('-')
                    quote = QuoteModel(words[0].strip(), words[1].strip())
                    quotes.append(quote)

        return quotes
