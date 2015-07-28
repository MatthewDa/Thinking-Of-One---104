from flask import Flask, render_template, request
import datetime
from util import *

app = Flask( __name__ )
inputTXT = ''

@app.route('/', methods=["POST","GET"])
def main():
    inputTXT = []
    if request.method == "GET":
        return render_template('xbasex.html', TXT="PlayerName")
    else:
        input_text = request.form
        append_file('log.txt')
        inputTXT.append(input_text['uInput'])
        print len(inputTXT)
        return render_template('xbasex.html', x=inputTXT, TXT = "Playername")

if __name__ == '__main__':
    app.debug = True
    app.run()
