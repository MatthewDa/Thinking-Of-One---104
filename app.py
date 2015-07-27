from flask import Flask, render_template, request
import datetime

<<<<<<< HEAD
app = Flask(__name__)
=======
app = Flask( __name__ )
inputTXT = ''
>>>>>>> d04a498cff4c4192bf20d11c441ac0342a40aa00

@app.route('/', methods=["POST","GET"])
def main():
<<<<<<< HEAD
    if request.method == "GET":
        return render_template('xbasex.html', TXT="PlayerName")
    else:
        input_text = request.form
        inputTXT = input_text['poop']
        return render_template('xbasex.html', x=inputTXT, TXT = "Playername")
=======

    inputTXT = []
    aform = request.form
    #return aform['asd']
    ##append to list
    inputTXT = inputTXT.append(aform['asd'])
    return render_template('base.html', inputTXT=inputTXT)
>>>>>>> d04a498cff4c4192bf20d11c441ac0342a40aa00

if __name__ == '__main__':
    app.debug = True
    app.run( port = 4269 )