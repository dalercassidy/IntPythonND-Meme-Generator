class QuoteModel:
    """Represents author and body of a quote."""

    def __init__(self, body, author):
        """Initialize quote.

        Arguments:
            body (str) - the quote itself
            author (str) - author of quote
        """
        self.body = body.strip('"')
        self.author = author

    def __str__(self):
        """Represent class by string."""
        return f'"{self.body}"- {self.author}'
