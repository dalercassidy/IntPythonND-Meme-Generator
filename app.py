import random
import os
import requests
import shutil
from flask import Flask, render_template, abort, request
from os import listdir

from MemeEngine import MemeEngine
from QuoteEngine import Ingestor

app = Flask(__name__)
meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []

    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    imgs = []
    for image in os.listdir(images_path):
        if (image.endswith(".jpg")):
            imgs.append(images_path + image)

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)

@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""    
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    tmp = f'./tmp/{random.randint(0,1000000)}.jpg'
    r = requests.get(image_url, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(tmp, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    meme = MemeEngine('./static')
    path = meme.make_meme(tmp, body, author)

    os.remove(tmp)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
