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
    g = f.read()
    h = g.split('\n')
    var = ' '.join(h)
    f.close()
    return var
def parse():
    f = open( 'Commands.txt', 'r' )
    text = f.read()
    text = text.split(',')
    f.close()
    inputTXT = 'use'
    i = 0
    while i <= len(text):
        #for commands in text:
        if inputTXT != text[i] or i > len(text):
            return 'foo'
        elif inputTXT == text[i]:
            return 'hi'
        elif inputTXT != text[i] and i <= len(text):
            i +=1
        
