from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Parses a CSV file."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Create a list of quotes from lines in a CSV file.

        Arguments:
            path (str) - the path of the csv file
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot parse csv file.')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            quotes.append(quote)

        return quotes
