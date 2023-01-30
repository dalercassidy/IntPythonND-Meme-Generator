MEME GENERATOR
--------------

Overview:
The project is a multimedia application that dynamically generates memes with an image overlaid with a quote.

Quotes are loaded from the filetypes- csv, docx, pdf and txt. A strategy object properly ingests the correct format. 
A quote and it's author are then randomly placed on the image. The text is randomly placed on the image starting
in the top left corner of the image in an effort to overlay as much of the quote as possible onto the image.

The program accepts user input via the command line and a flask web service.

Commandline Interface:
----------------------
Accepts 3 optional arguments of body, author and image. If any of the arguments are missing, random selections are 
made.

Example runs:
```
python meme.py --path "_data\photos\dog\xander_1.jpg" 
python meme.py --path "_data\photos\dog\xander_1.jpg" --author "me" --body "Enjoying Life"
```

Flask Web Service:
------------------
The web service accepts 3 arguments of body, author and image url. The image url is a url to an image that is
downloaded and then overlaid with quote and author.

The flask web service is defined in app.py. Execute app.py and go to the given local url provided by the program
to execute the service.

Dependency:
flask

Modules and Dependencies:
-------------------------

MemeEngine Module:
MemeEngine has a class called MemeEngine. The MemeEngine class is used to create a meme.
The function "def make_meme(self, img_path, text, author, width=500) -> str:" returns the path
to a new meme image. Inputs to the function are the path of the image, the quote, author and width to
resize the new image to which defaults to 500.

Dependencies include the Pillow Module to manipulate images. 

QuoteEngine Module:
Used to generate quotes.

Has an abstract class called IngestorInterface that has 2 abstract methods:
1) def can_ingest(cls, path) -> bool
Returns whether or not the class can parse the given file's type.
2) def parse(cls, path: str) -> List[QuoteModel]
Used to parse the file type

PDFIngestor, TextIngestor, CSVIngestor and DocxIngestor inherit IngestorInterface
and define the can_ingest and parse methods of the parent to parse their
appropriate filetypes. Ingestor is a class that chooses the correct strategy to use
to parse a file. All classes return a list of Quotes. The quote is defined by the QuoteModel 
class with an author and a body.

Dependencies:
CSVIngestor - pandas
DocxIngestor - docx
PDFIngestor - uses subprocess to call pdftotext executable in xpdf library

Examples on How to Use Modules:
-------------------------------

Example to print out all the quotes in a text file using Ingestor in QuoteEngine module:
```
for q in Ingestor.parse(r'.\_data\DogQuotes\DogQuotesTXT.txt'):
    print(q)
```
Example to create a meme in the tmp directory with awidth of 380 using MemeEngine module:
```
m = MemeEngine('./tmp')
m.make_meme('./_data/photos/dog/xander_1.jpg', "You must be the change you wish to see in the world.", "Gandhi", width=380)
```

