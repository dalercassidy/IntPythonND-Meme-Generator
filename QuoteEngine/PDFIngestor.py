from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Parses a pdf file."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Create a list of quotes from lines in a pdf file.

        Arguments:
            path (str) - the path of the pdf file.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot parse pdf file.')
        tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        quotes = []

        with open(tmp, 'r', encoding="utf-8-sig") as f:
            for line in f:
                formatted_line = line.strip('\r\n').strip()
                if len(formatted_line):
                    words = formatted_line.split('"')
                    index = 1
                    while index < len(words):
                        quote = QuoteModel(
                                words[index].strip(),
                                words[index+1].strip(' -')
                            )
                        quotes.append(quote)
                        index += 2
        os.remove(tmp)
        return quotes
