import time
import sys

if sys.platform.startswith('java'):
    #import pyautogui._pyautogui_java as platformModule
    raise NotImplementedError('Jython is not yet supported by PyAutoGUI.')
elif sys.platform == 'darwin':
    import pyautogui._pyautogui_osx as platformModule
elif sys.platform == 'win32':
    import pyautogui._pyautogui_win as platformModule
else:
    import pyautogui._pyautogui_x11 as platformModule

def press(keys, presses=1, interval=0.0, pause=None, _pause=True):
    """Performs a keyboard key press down, followed by a release.

    Args:
      key (str, list): The key to be pressed. The valid names are listed in
      KEYBOARD_KEYS. Can also be a list of such strings.
      presses (integer, optiional): the number of press repetition
      1 by default, for just one press
      interval (float, optional): How many seconds between each press.
      0.0 by default, for no pause between presses.
      pause (float, optional): How many seconds in the end of function process.
      None by default, for no pause in the end of function process.
    Returns:
      None
    """
    if type(keys) == str:
        keys = [keys] # put string in a list
    else:
        lowerKeys = []
        for s in keys:
            if len(s) > 1:
                lowerKeys.append(s.lower())
            else:
                lowerKeys.append(s)
    interval = float(interval)
    for i in range(presses):
        for k in keys:
            platformModule._keyDown(k)
            platformModule._keyUp(k)
        time.sleep(interval)

    if pause is not None and _pause:
        time.sleep(pause)
    elif _pause and PAUSE != 0:
        time.sleep(PAUSE)

def typewrite(message, interval=0.1, pause=True, _pause=True):
    """Performs a keyboard key press down, followed by a release, for each of
    the characters in message.

    The message argument can also be list of strings, in which case any valid
    keyboard name can be used.

    Since this performs a sequence of keyboard presses and does not hold down
    keys, it cannot be used to perform keyboard shortcuts. Use the hotkey()
    function for that.

    Args:
      message (str, list): If a string, then the characters to be pressed. If a
        list, then the key names of the keys to press in order. The valid names
        are listed in KEYBOARD_KEYS.
      interval (float, optional): The number of seconds in between each press.
        0.0 by default, for no pause in between presses.

    Returns:
      None
    """
    interval = float(interval)

    for c in message:
        if len(c) > 1:
            c = c.lower()
        press(c, _pause=False)
        time.sleep(interval)

    if pause is not None and _pause:
        time.sleep(pause)
    elif _pause and PAUSE != 0:
        time.sleep(PAUSE)

