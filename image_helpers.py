from PIL import Image
import StringIO
import random
import os

from cache import cache


def create_image(width, height):
    stringfile = StringIO.StringIO()
    im = Image.open(choose_image(width, height))
    resize(im, width, height)
    im = im.crop((0, 0, int(width), int(height)))
    im.save(stringfile, 'JPEG')
    return stringfile


def choose_image(width, height):
    if is_portrait(width, height):
        images = list_portraits()
    elif is_square(width, height):
        images = list_squares()
    elif is_landscape(width, height):
        images = list_landscapes()
    return random.choice(images)


def resize(im, width, height):
    width_box, height_box = int(width), int(height)
    ratio_box = calculate_ratio((width_box, height_box))
    ratio_im = calculate_ratio(im.size)

    if ratio_im < ratio_box:
        width_box = height_box * (1 / ratio_im)
    elif ratio_im > ratio_box:
        height_box = width_box * ratio_im

    im.thumbnail((width_box, height_box), Image.ANTIALIAS)
    return im


def calculate_ratio(size):
    width, height = float(size[0]), float(size[1])
    return height / width


def is_portrait(width, height):
    output = width < height
    return output


def is_landscape(width, height):
    return width > height


def is_square(width, height):
    return width == height


def list_squares():
    return list_files("puppies/squares")


def list_portraits():
    return list_files("puppies/portraits")


def list_landscapes():
    return list_files("puppies/landscapes")


@cache.memoize()
def list_files(path):
    images = []
    for filename in os.listdir(path):
        if filename.endswith(".jpg"):
            images.append(path + "/" + filename)
    return images
