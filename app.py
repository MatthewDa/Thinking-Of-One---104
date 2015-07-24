from flask import Flask, render_template, request
from util import *
import datetime
import urllib2
from urllib import urlencode

if __name__ == '__main__':
    app.debug = True
    app.run( port = 4269 )

app = Flask( __name__ )

@app.route('/', methods=["GET","POST"])
def main():
    return render_template('index.html')
