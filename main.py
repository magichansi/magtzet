from flask import Flask

app = Flask(__name__)


@app.route('/')
def mainroute():
    return 'magtzet'

app.run()