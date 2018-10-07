#/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config.from_pyfile('app.cfg')
pages = FlatPages(app)

@app.route("/")
def index():
    return "À noite, vovô Kowalsky vê o ímã cair no pé do pinguim queixoso e vovó põe açúcar no chá de tâmaras do jabuti feliz."

@app.route("/<path:path>/")
def page(path):
    print(pages.get_or_404(path).meta)
    return pages.get_or_404(path).html

if __name__ == "__main__":
    app.run(port=5000)
