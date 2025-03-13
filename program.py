from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>once i was a 7 years old i sat on a banana and that changed my life</p>"

@app.route("/national_slave_farm")
def national_slave_farm():
    return "<p>pls master leave me alone. GET BACK TO WORK MONKEY</p>"


