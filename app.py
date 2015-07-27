from flask import Flask, render_template, request
import datetime
from util import *

app = Flask( __name__ )
inputTXT = ''

@app.route('/', methods=["GET","POST"])
def main():

    inputTXT = []
    aform = request.form
    #return aform['asd']
    ##append to list
    inputTXT = inputTXT.append(aform['asd'])
    return render_template('base.html', inputTXT=inputTXT)

if __name__ == '__main__':
    app.debug = True
    app.run( port = 4269 )
