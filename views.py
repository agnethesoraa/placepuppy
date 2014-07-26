from flask import Flask, render_template, make_response
from image_helpers import create_image
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<width>x<height>')
@app.route('/<width>X<height>')
@app.route('/<width>x<height>/')
@app.route('/<width>X<height>/')
def serve_image(width, height):
    stringfile = create_image(width, height)
    response = make_response(stringfile.getvalue())
    response.headers["Content-Type"] = "image/jpeg"
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
