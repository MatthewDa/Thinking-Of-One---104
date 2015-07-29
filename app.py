from flask import Flask, render_template, request
import datetime
from util import *

app = Flask( __name__ )
clear_file()
commands = 'Valid commands include up, down, left, right, look, use, help, open, clear, and get. Some require the use of an item while others are custom to the location.'

@app.route('/', methods=["GET"])
def main():
    inputTXT = ''
    outputTXT = ''
    story = ''
    user = 'fooman'
    bot = ''
    return render_template('main.html', TXT=user)    

@app.route('/basement/', methods=["POST","GET"])
def basement():
    inputTXT = ''
    outputTXT = ''
    story = ''
    user = 'fooman'
    bot = ''
    
    if request.method == "GET":
        clear_file()
        story = 'You are stuck in a dark room.'
        outputTXT = open_file( 'log.txt', outputTXT )
        return render_template('xbasex.html', story = story, out = outputTXT, TXT=user) 
    else:
        story = 'You are stuck in a dark room.'
        input_text = request.form
        inputTXT = input_text['uInput']

        if inputTXT == 'help':
            bot = commands
        if inputTXT == 'clear':
            clear_file()
            
        if inputTXT == 'look':
            bot = 'You scramble about and find a few items around you: a match and a candle.'           
        if inputTXT == 'use candle':
            bot = 'You light the candle using the match.'
            story = 'You see the room more clearly. You find that you are in a basement, filled with boxes. <br>\n Looking through the room, you find a stairway. However, you find that it is locked. Maybe if you had a key, you would be able to escape the basement.'
        if inputTXT == 'look box':
            bot = 'You find a key that looks familiar.'
            story = 'This key would likely be able to allow you to exit the basement.'
        if inputTXT == 'use key':
            bot = "You used the key on the basement door."
            story = "The door opens. You can now go up and exit the basement."
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
        clear_file()
        story = 'You find that you are in a shed. There are tools and equipment on the floor: a shovel, boots, and a coat.'
        outputTXT = open_file( 'log.txt', outputTXT )
        return render_template('xbase.html', story = story, out = outputTXT, TXT=user)
    
    else:
        story = 'You find that you are in a shed. There are tools and equipment on the floor: a shovel, boots, and a coat.'
        input_text = request.form
        inputTXT = input_text['uInput']

        if inputTXT == 'help':
            bot = commands
        if inputTXT == 'clear':
            clear_file()
            
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
        if inputTXT == 'up':
            bot = 'You exit the shed.'
            story = 'You find yourself confused as to where you are. You find that it is night and you are stuck in the woods. <br>\nFeral wolves wander towards you.'
        if inputTXT == 'use shovel':
            bot = 'You whack their heads and they pass out.'
            story = 'You start to wander the area and you find a way out, but it is blocked by an armored bear. You need to hit that bear 3 times with the shovel.'
        if inputTXT == 'use shovel 3 times':
            bot = 'You managed to defeat the bear. You can now leave the area.'
            bot += "<a href= '/city/'>The City</a>"
        append_file('log.txt', inputTXT, bot )
        outputTXT = open_file( 'log.txt', outputTXT)

        return render_template('xbase.html', story = story, out = outputTXT, TXT = user)

@app.route('/city/', methods=["POST","GET"])
def city():
    inputTXT = ''
    outputTXT = ''
    story = ''
    user = 'fooman'
    bot = ''
    
    
    if request.method == "GET":
        clear_file()
        story = 'You enter the city and find that it is abandoned.'
        outputTXT = open_file( 'log.txt', outputTXT )
        return render_template('base.html', story = story, out = outputTXT, TXT=user)
    
    else:
        story = 'You enter the city and find that it is abandoned.'
        input_text = request.form
        inputTXT = input_text['uInput']


        if inputTXT == 'help':
            bot = commands
        if inputTXT == 'clear':
            clear_file()
            
        if inputTXT == 'down':
            bot = "You go back to the woods."
            bot += "<a href= '/woods/'>The Woods</a>"
        if inputTXT == 'look':
            bot = 'You find a long carved wooden staff.'
            story = 'As you are scavenging, you hear heavy grunting and breathing. You look outside and find the city infested with zombies. A few zombies block the way out. You decide to fight them.'
        if inputTXT == 'use staff':
            bot == 'You wave the staff like a lunatic. It does nothing but attract zombies.'
            story == 'The zombies grow closer.'
        if inputTXT == 'use shovel':
            bot == 'The zombie heads are quick work with your shoveling skills and they are easily defeated. '
            story == 'The city seems more abandoned now.'
        if inputTXT == 'up':
            bot == 'You see a mansion above you in the distance. You decide to go there.'
            bot += "<a href= '/mansion/'>The Mansion</a>"
        append_file('log.txt', inputTXT, bot )
        outputTXT = open_file( 'log.txt', outputTXT)

        return render_template('base.html', story = story, out = outputTXT, TXT = user)

@app.route('/mansion/', methods=["POST","GET"])
def mansion():
    inputTXT = ''
    outputTXT = ''
    story = ''
    user = 'fooman'
    bot = ''
    
    
    if request.method == "GET":
        clear_file()
        story = 'You see lots of furniture, covered with blankets of dust and infested with small insects.'
        outputTXT = open_file( 'log.txt', outputTXT )
        return render_template('basex.html', story = story, out = outputTXT, TXT=user)
    
    else:
        story = 'You see lots of furniture, covered with blankets of dust and infested with small insects.'
        input_text = request.form
        inputTXT = input_text['uInput']

        if inputTXT == 'help':
            bot = commands
        if inputTXT == 'clear':
            clear_file()
            
        if inputTXT == 'down':
            bot = "You go back down to the city."
            bot += "<a href= '/city/'>The City</a>"
        if inputTXT == 'up':
            bot = "You sense that you aren't alone anymore."
            story = "You see a door that leads to a maze. Looks like there is a golden shovel there. Shiny."
        if inputTXT == 'open door':
            bot = "The door doesn't open. Something taps your shoulder. You turn to find ghosts."
            story = "Defeat the ghosts to get to the maze."
        if inputTXT == 'use shovel':
            bot = 'It passes right through them.'
            story = 'The ghosts start to surround you.'
        if inputTXT == 'use staff':
            bot = 'The ghosts fizzle out and disappear.'
            story = 'The doors click open. You can go drop down to the maze.'
        if inputTXT == 'down':
            bot = 'You jump down to the maze.'
            bot += "<a href= '/maze/'>The Maze</a>"
        append_file('log.txt', inputTXT, bot )
        outputTXT = open_file( 'log.txt', outputTXT)

        return render_template('basex.html', story = story, out = outputTXT, TXT = user)

@app.route('/maze/', methods=["POST","GET"])
def maze():
    inputTXT = ''
    outputTXT = ''
    story = ''
    user = 'fooman'
    bot = ''
    
    if request.method == "GET":
        clear_file()
        story = 'You find that you are in a shed. There are tools and equipment on the floor: a shovel, boots, and a coat.'
        outputTXT = open_file( 'log.txt', outputTXT )
        return render_template('base_.html', story = story, out = outputTXT, TXT=user)
    
    else:
        story = 'You find that you are in a shed. There are tools and equipment on the floor: a shovel, boots, and a coat.'
        input_text = request.form
        inputTXT = input_text['uInput']

        if inputTXT == 'help':
            bot = commands
        if inputTXT == 'clear':
            clear_file()
        
        if inputTXT == 'up':
            bot = "You go up back into the mansion."
            bot += "<a href= '/mansion/'>The Mansion</a>"
        if inputTXT == 'look':
            bot = "You see two paths ahead of you."
            story = "There are two paths ahead of you: a red path and a blue path. Each path will lead you somewhere."
        if inputTXT == 'blue path':
            bot = "You take the blue path and get ambushed by bandits. You die."
            bot += "<a href= '/maze/'>Try again?</a>"
        if inputTXT == 'red path':
            bot = "You take the right path and continue onwards into the maze."
            story = "Two more paths appear ahead of you now: a path that has a sign with an emblem of a falcon and a path that has a sign with an emblem of a fox. Each path will lead you somewhere."
        if inputTXT == "falcon path":
            bot = "You take the right path again and continue onwards into the maze."
            story = "You are almost to your golden shovel!!! The last two paths appear before you:"
        if inputTXT == "fox path":
            bot = "You take the fox path and your eyes are scratched out by a fox. You die."
            bot += "<a href= '/maze/'>Try again?</a>"
        i
        append_file('log.txt', inputTXT, bot )
        outputTXT = open_file( 'log.txt', outputTXT)

        return render_template('base_.html', story = story, out = outputTXT, TXT = user)

if __name__ == '__main__':
    app.debug = True
    app.run()
