from PIL import Image
import StringIO


def create_image(width, height):
    stringfile = StringIO.StringIO()
    im = Image.open(choose_image(width, height))
    im.thumbnail((int(width), int(height)), Image.ANTIALIAS)
    im = im.crop((0, 0, int(width), int(height)))
    im.save(stringfile, 'JPEG')
    return stringfile


def is_portrait(width, height):
    return height > width


def is_square(width, height):
    return width == height


def is_landscape(width, height):
    return height < width


def list_squares():
    return ["puppies/squares/S001.jpg", "puppies/squares/S002.jpg",
            "puppies/squares/S003.jpg"]


def list_portraits():
    return ["puppies/portraits/P001.jpg", "puppies/portraits/P002.jpg",
            "puppies/portraits/P003.jpg"]


def list_landscapes():
    return ["puppies/landscapes/L001.jpg", "puppies/landscapes/L002.jpg",
            "puppies/landscapes/L003.jpg"]


def choose_image(width, height):
    if is_portrait(width, height):
        images = list_portraits()
    elif is_square(width, height):
        images = list_squares()
    elif is_landscape(width, height):
        images = list_landscapes()
    return images[0]
