from flask import Flask, render_template
import testing

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("begin.html")

@app.route("/game/")
def game():
    return testing.ep1()

if __name__ == '__main__':
    app.debug = True
    app.run()
