import time
import sys

def demo(uinput):
    item = uinput
    str1 = delay_type('Hello, traveler.\n', interval=0.1)
    str2 = delay_type('I see you want ' + item + '.', interval=.25)

def delay_type(str, interval):
    for letter in str:
        sys.stdout.write(letter)
        time.sleep(interval)

def append_file( fname, text ):
    f = open( fname, 'a' )
    f.write(text+'\n')
    f.close()

def open_file( fname, var ):
    f = open( fname, 'r' )
    var = f.read()
    f.close()

def parse():
    f = open( 'Commands.txt', 'r' )
    text = f.read()
    text = text.split(',')
    f.close()
    #return text
    inputTXT = 'down'
    if inputTXT == text:
        return 'hi'
    else:
        return 'Really?'
