from flask import Flask, render_template, request
import datetime
from util import *

app = Flask( __name__ )

@app.route('/', methods=["GET","POST"])
def main():
    return render_template('base.html')
    form = request.form
    uInput = form['asd']
        if uInput == '':
            inputTXT = 'fooooooo'
            return render_template('base.html', inputTXT=inputTXT)
        elif request.method == 'POST':
            inputTXT = 'hello'
            return render_template('base.html', inputTXT=inputTXT)
        elif request.method == 'GET':
            inputTXT = 'foo'
            return render_template('base.html', inputTXT=inputTXT)

if __name__ == '__main__':
    app.debug = True
    app.run( port = 4269 )
