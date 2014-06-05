from flask import Flask, render_template, make_response
from PIL import Image
import StringIO
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<width>x<height>')
@app.route('/<width>X<height>')
def serve_image(width, height):
    stringfile = StringIO.StringIO()
    im = Image.open("static/images/annie.jpg")
    im.thumbnail((int(width), int(height)), Image.ANTIALIAS)
    im = im.crop((0, 0, int(width), int(height)))
    im.save(stringfile, 'JPEG')
    response = make_response(stringfile.getvalue())
    response.headers["Content-Type"] = "image/jpeg"
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
