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

def append_file( fname ):
    f = open( fname, 'a' )
    text = f.read()
    f.close()
    return text
