from flask import Flask, render_template, request
import datetime
from util import *

app = Flask( __name__ )
inputTXT = ''

@app.route('/', methods=["POST","GET"])
def main():
    inputTXT = []
    outputTXT = ''
    user = 'fooman'
    if request.method == "GET":
        return render_template('xbasex.html', TXT=user)
    else:
        input_text = request.form
        inputTXT = input_text['uInput']
        append_file('log.txt', inputTXT)
        outputTXT = open_file( 'log.txt', outputTXT )

        return render_template('xbasex.html', x=outputTXT, TXT = user)

if __name__ == '__main__':
    app.debug = True
    app.run()
