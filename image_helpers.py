from PIL import Image
import StringIO
import random
import os

from cache import cache


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
    return list_files("puppies/squares")


def list_portraits():
    return list_files("puppies/portraits")


def list_landscapes():
    return list_files("puppies/landscapes")


@cache.memoize()
def list_files(path):
    images = []
    print path
    for filename in os.listdir(path):
        if filename.endswith(".jpg"):
            images.append(path + "/" + filename)
    return images


def choose_image(width, height):
    if is_portrait(width, height):
        images = list_portraits()
    elif is_square(width, height):
        images = list_squares()
    elif is_landscape(width, height):
        images = list_landscapes()
    return random.choice(images)
