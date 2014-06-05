from PIL import Image
import StringIO


def create_image(width, height):
    stringfile = StringIO.StringIO()
    im = Image.open("static/images/annie.jpg")
    im.thumbnail((int(width), int(height)), Image.ANTIALIAS)
    im = im.crop((0, 0, int(width), int(height)))
    im.save(stringfile, 'JPEG')
    return stringfile
