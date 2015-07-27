from flask import Flask, render_template, request
import datetime
from util import *

app = Flask( __name__ )

@app.route('/', methods=["GET","POST"])
def main():

    uInput = ''
    if uInput == '':
        aform = request.form
        uInput = aform['asd']
        inputTXT = uInput
        return render_template('base.html', inputTXT=inputTXT)
        aform = request.form
        uInput = aform['asd']
        
    elif request.method == 'GET':
        aform = request.form
        uInput = aform['asd']
        inputTXT = 'foo'
        return render_template('base.html', inputTXT=inputTXT)
        aform = request.form
        uInput = aform['asd']
    elif uInput
        aform = request.form
        uInput = aform['asd']
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
