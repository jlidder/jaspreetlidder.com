from flask import Flask, Response
import os
app = Flask(__name__)

# Used code bit from : http://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))

# Used code bit from : http://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()
    except IOError as exc:
        return str(exc)

@app.route("/")
def hello():
    content = get_file('index.html')
    return Response(content, mimetype="text/html")

