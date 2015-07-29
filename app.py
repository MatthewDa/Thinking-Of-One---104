from flask import Flask, render_template, request
import datetime
from util import *

app = Flask( __name__ )

clear_file()

@app.route('/', methods=["POST","GET"])
def main():
    render_template('main.html')    

@app.route('/basement/', methods=["POST","GET"])
def basement():
    inputTXT = ''
    outputTXT = ''
    story = ''
    user = 'fooman'
    bot = ''
    
    if request.method == "GET":
        story = 'You are stuck in a dark room.'
        outputTXT = open_file( 'log.txt', outputTXT )
        return render_template('xbasex.html', story = story, out = outputTXT, TXT=user) 
    else:
        story = 'You are stuck in a dark room.'
        input_text = request.form
        inputTXT = input_text['uInput']

        if inputTXT == 'help':
            bot = parse(inputTXT, bot)
        if inputTXT == 'look':
            bot = 'You scramble about and find a few items around you: a match and a candle.'           
        if inputTXT == 'use match':
            bot = 'You light the match.'
        if inputTXT == 'use candle':
            bot = 'You light the candle.'
            story = 'You see the room more clearly. You find that you are in a basement, filled with boxes. <br>\n Looking through the room, you find a stairway. However, you find that it is locked. Maybe if you had a key, you would be able to escape the basement.'
        if inputTXT == 'look box':
            bot = 'You find a key that looks familiar.'
            story = 'This key would likely be able to allow you to exit the basement.'
        if inputTXT == 'use key':
            bot = "You used the key on the basement door."
            story = "You go up the stairway and use they key. You can now exit the basement."
        if inputTXT == 'up':
            bot = "You exit the basement."
            bot += "<a href= '/woods/'>The Woods</a>"
            
        append_file('log.txt', inputTXT, bot )
        outputTXT = open_file( 'log.txt', outputTXT)

        return render_template('xbasex.html', story = story, out = outputTXT, TXT = user)

@app.route('/woods/', methods=["POST","GET"])
def woods():
    inputTXT = ''
    outputTXT = ''
    story = ''
    user = 'fooman'
    bot = ''
    
    
    if request.method == "GET":
        story = 'You find that you are in a shed. There are tools and equipment on the floor: a shovel, boots, and a coat.'
        outputTXT = open_file( 'log.txt', outputTXT )
        return render_template('xbase.html', story = story, out = outputTXT, TXT=user)
    
    else:
        story = 'You find that you are in a shed. There are tools and equipment on the floor: a shovel, boots, and a coat.'
        input_text = request.form
        inputTXT = input_text['uInput']
        
        if inputTXT == 'down':
            bot = "You go down to the basement."
            bot += "<a href= '/basement/'>The Basement</a>"
        if inputTXT == 'get shovel':
            bot = 'You arm yourself with the shovel.'
        if inputTXT == 'get boots':
            bot = 'You put on the boots.'
        if inputTXT == 'get coat':
            bot = 'You put on the coat.'
            story = "There's a giant rat on the floor."
        if inputTXT == 'use shovel':
            bot = 'You whack the giant rat with your shovel. It skitters away.'
            
        append_file('log.txt', inputTXT, bot )
        outputTXT = open_file( 'log.txt', outputTXT)

        return render_template('xbasex.html', story = story, out = outputTXT, TXT = user)

    
if __name__ == '__main__':
    app.debug = True
    app.run()
