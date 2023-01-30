from PIL import Image, ImageDraw, ImageFont
import random


class MemeEngine:
    """Creates meme image with caption."""

    def __init__(self, output_dir):
        """Initialize Meme.

        Arguments:
            output_dir (str) - output dir of new meme image
        """
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a captioned meme image from provided image and quote.

        Arguments:
            img_path (str) - the path of the csv file
            text (str) - quote
            author (str) - author of quote
            width (int) - width to resize image to
        """        
        # Loading image file
        img = Image.open(img_path)
        try:
            img = Image.open(img_path)
        except Exception:
            raise Exception(f'Unable to load image at {img_path}')

        # Transform image by resizing to a maximum width of 500px
        # while maintaining the input aspect ratio

        if width is None or width > 500 or width < 10:
            raise Exception("Invalid width for resizing image.")

        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)
   
        # Add a caption to an image (string input) with a body
        # and author to a random location on the image.
        # random_x is no more than half of the width to 
        # have enough room to print message.
        # random_y is no more than half of the height to
        # have enough room to print message.

        random_x = int(random.randint(0, width-1) / 2)
        random_y = int(random.randint(0, height-1) / 2)

        if text is not None:
            message = f'"{text}"'

        if author is not None:
            message += f' - {author}'

        if message is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
            draw.text((random_x, random_y), message, font=font, fill='white')

        tmp = f'{self.output_dir}/{random.randint(0,1000000)}.jpg'
        img.save(tmp)

        return tmp
