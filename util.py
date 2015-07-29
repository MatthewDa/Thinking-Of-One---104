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

def append_file( fname, text, bot):
    f = open( fname, 'a' )
    f.write( '>>>' + text + '<br>\n' )
    f.write( bot + '<br>\n' )
    f.close()

def open_file( fname, var ):
    f = open( fname, 'r' )
    var = f.read()
    return var

def clear_file():
    f = open( 'log.txt', 'w' )
    f.write( '' )
    f.close()

def commands(var):
    f = open( 'Commands.txt', 'r' )
    text = f.read()
    text = text.split(',')
    f.close()
    var = "Valid commands include " + ', '.join(text) + '.'
    return var
##    while i <= len(text):
##        try:
##            if var == 'help':
##                var2 = cmnds
##            elif var == 'clear':
##                clear_file()
##            elif var == text[i]:
##                return True
##            
##        except IndexError or UnboundLocalError:
##            return "That's an invalid command. Type help for commands."
