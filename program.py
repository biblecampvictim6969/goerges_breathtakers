from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>once i was a 7 years old i sat on a banana and that changed my life</p>"

