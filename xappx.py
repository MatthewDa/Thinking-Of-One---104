from flask import Flask, render_template, request
import datetime
from util import *

app = Flask( __name__ )
inputTXT = ''

@app.route('/', methods=["GET","POST"])
def main():
    aform = request.form
    inputTXT = inputTXT.append(aform['poop'])
    return render_template('xbasex.html', inputTXT=inputTXT)
    
if __name__ == '__main__':
    app.debug = True
    app.run( port = 4269 )
