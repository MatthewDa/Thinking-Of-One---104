from flask import Flask, render_template, request
import datetime
from util import *

app = Flask( __name__ )

@app.route('/', methods=["GET","POST"])
def main():

    uInput = ''
    if uInput == '':
        inputTXT = uInput
        return render_template('base.html', inputTXT=inputTXT)
        aform = request.form
        uInput = aform['asd']
    elif request.method == 'GET':
        inputTXT = 'foo'
        return render_template('base.html', inputTXT=inputTXT)
        aform = request.form
        uInput = aform['asd']
    elif uInput == '':
        inputTXT = uInput
        return render_template('base.html', inputTXT=inputTXT)
        aform = request.form
        uInput = aform['asd']
    elif request.method == 'POST':
        inputTXT = 'hello'
        return render_template('base.html', inputTXT=inputTXT)
        aform = request.form
        uInput = aform['asd']

if __name__ == '__main__':
    app.debug = True
    app.run( port = 4269 )
