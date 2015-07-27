from flask import Flask, render_template, request
import datetime
from util import *

app = Flask( __name__ )

@app.route('/', methods=["GET","POST"])
def main():
    if request.method == 'GET':
        return render_template('base.html')
    elif request.method == 'POST':
        uInput = request.form
        inputTXT = uInput['asd']
        return render_template('base.html', inputTXT=inputTXT)
if __name__ == '__main__':
    app.debug = True
    app.run( port = 4269 )
