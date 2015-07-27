from flask import Flask, render_template, request
import datetime
import util

app = Flask( __name__ )

@app.route('/')

def main():
    return render_template('base.html', inputTXT=returnTXT())

if __name__ == '__main__':
    app.debug = True
    app.run( port = 4269 )

