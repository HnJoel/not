
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>so that at the name of Jesus every knee should bow, in heaven and on earth and under the earth.(Philippians2:10 ESV)</p>"
