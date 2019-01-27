#!/usr/bin/python
from flask import Flask,Response

app = Flask(__name__)


@app.route('/')
def mainroute():
    return Response("magtzet")

if __name__ == "__main__":
    app.run()
