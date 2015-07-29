import easygui

title = "Game"

def ep1():
    choice1 = easygui.choicebox('You are stuck in a dark room. You scramble about and find a few items around you: a match and a candle.', title, choices = ['light the candle','leave the room'])
    if choice1 == 'light the candle':
        return ep2()
    else:
        easygui.msgbox('The door is locked')
        return ep1()

def ep2():
    choice2 = easygui.choicebox('You light the candle and see the room more clearly. You find that you are in a basement, filled with boxes.', title, choices = ['look around','let the fire burn'])
    if choice2 == choice2[0]:
        return ep3()
    else:
        return ep1()
