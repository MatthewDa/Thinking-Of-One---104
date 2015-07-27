from flask import Flask, render_template, request
import datetime
from util import *

app = Flask( __name__ )

@app.route('/', methods=["GET","POST"])
def main():
    return render_template('base.html')
    
@app.route('/', methods=["POST"])
def text():
    inputTXT = request.form['asd']
    return inputTXT
    

if __name__ == '__main__':
    app.debug = True
    app.run( port = 4269 )
