import pyautogui

def demo(uinput):
    item = uinput
    pyautogui.typewrite('Hello, traveler.', interval=0.1)
    pyautogui.press('enter', interval=1)
    pyautogui.typewrite('I see you want ' + item + '.', interval=.25)
##        return 'Pressed Enter?'

def prompts():
    pyautogui.alert('This displays some text with an OK button.')
    pyautogui.confirm('This displays text and has an OK and Cancel button.')
    prompt = pyautogui.prompt('This lets the user type in a string and press OK.')

