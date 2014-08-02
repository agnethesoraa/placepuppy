from PIL import Image

from image_helpers import calculate_ratio, resize, is_portrait, is_landscape


def test_calculate_ratio():
    assert calculate_ratio((1, 1)) == 1
    assert calculate_ratio((1, 2)) == 2
    assert calculate_ratio((2, 1)) == 0.5


def test_is_portrait():
    assert is_portrait(200, 400)
    assert not is_portrait(400, 200)
    assert not is_portrait(1, 1)


def test_is_landscape():
    assert is_landscape(400, 200)
    assert not is_landscape(200, 400)
    assert not is_landscape(1, 1)


def test_resize_ratio_box_bigger_than_ratio_im():
    height = 250
    width = 100
    im = Image.open('static/images/annie.jpg')
    resized_im = resize(im, width, height)
    assert resized_im.size[0] >= width
    assert resized_im.size[1] == height


def test_resize_ratio_box_smaller_than_ratio_im():
    height = 250
    width = 230
    im = Image.open('static/images/annie.jpg')
    resized_im = resize(im, width, height)
    assert resized_im.size[0] == width
    assert resized_im.size[1] >= height
