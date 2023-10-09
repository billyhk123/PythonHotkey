import sys
import keyboard
import os
import pyperclip
import time

def print_pressed_keys(e):
        line = ', '.join(str(code) for code in keyboard._pressed_events)
        # '\r' and end='' overwrites the previous line.
        # ' '*40 prints 40 spaces at the end to ensure the previous line is cleared.
        print('\r' + line + ' ', end='')

        #for i in keyboard._os_keyboard.from_name:
                #print(i)

def on_key_press(event):
            print(event.name)

def open_notepad():
    os.startfile('C:/Windows/system32/notepad.exe')

clipBroadStack = ["Ori_1", "Ori_2", "Ori_3", "Ori_4", "Ori_5", "Ori_6", "Ori_7", "Ori_8", "Ori_9", "Ori_10"]

def push_stack():
    time.sleep(.01)
    value = pyperclip.paste()
    global clipBroadStack            
    if len(clipBroadStack) == 10:
        # If the stack size is already 10, remove the oldest element from the stack        
        clipBroadStack.pop(0)
    # Add the new element to the top of the stack
    if value != "":
        clipBroadStack.append(value)
    else:
        print("Cannot handle empty string")

    storeClipboard(value)

def storedClipbroad():
        print(clipBroadStack)


def getClipValue(v):
        keyboard.write(clipBroadStack[v])

storedClipboard = ""
def storeClipboard(c):
        global storedClipboard
        storedClipboard = c
        print("storedClipboard is " + storedClipboard)

def printClipboardText():
        keyboard.write(storedClipboard.strip())
        print(clipBroadStack)

def checkClip():
        print("The current clip is :" + pyperclip.paste())
        

def connectSer():
        os.system('ROC_Billy.bat')

def main():
        
        keyboard.add_hotkey('ctrl+c', push_stack) #update the stack
        keyboard.add_hotkey('ctrl+shift+alt+v', printClipboardText)
        keyboard.add_hotkey('ctrl+shift+alt+1', getClipValue, args=[9])
        keyboard.add_hotkey('ctrl+shift+alt+2', getClipValue, args=[8])
        keyboard.add_hotkey('ctrl+shift+alt+3', getClipValue, args=[7])

        keyboard.add_hotkey('ctrl+shift+p', open_notepad)
        keyboard.add_hotkey('ctrl+shift+o', keyboard.write, args=[storedClipboard])
        keyboard.add_hotkey('ctrl+shift+i', os.system, args=['ROC_Billy.bat'])
        
        keyboard.add_abbreviation('ttkk', "Please feel free to let me know if you have any question.")
        keyboard.add_abbreviation('eenn', "Please feel free to let me know if anything else is needed.")
        keyboard.add_abbreviation('aatt', "Please find attached the ")
        keyboard.add_abbreviation('ttvv', "Thank you very much ")
        
        
        keyboard.add_abbreviation('=sum', "=sumifs(")
        keyboard.add_abbreviation('=coun', "=countifs(")
        keyboard.add_abbreviation('=xloo', "=xlookup(")
        keyboard.add_abbreviation('=vloo', "=vlookup(")

        instruction = "ttkk, Please feel free to let me know if you have any question \n eell, Please feel free to let me know if anything else is needed. \n  aatt, Please find attached the \n ttvv,  Thank you very much \n"
        keyboard.add_abbreviation('iiiddd', instruction)

        #keyboard.on_press(on_key_press)  # attach the function to the key press event

        print("HotKeys Started")

        #keyboard.hook(print_pressed_keys)
        keyboard.wait()  # wait for key events

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
            print(e)
            import ctypes  # An included library with Python install.   
            ret_val = ctypes.windll.user32.MessageBoxW(0, "HotKey occurs an error.", "ERROR", 1)


