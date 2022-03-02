from pad4pi import rpi_gpio
from pynput.keyboard import Key, Controller
import time
import RPi.GPIO as GPIO
import subprocess
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup Keypad
KEYPAD = [
        ["A","B","C","D"],
        ["1","2","3","4"],
        ["E","F","G","H"],
        ["5","6","7","8"]
]

# same as calling: factory.create_4_by_4_keypad, still we put here fyi:
ROW_PINS = [26, 19, 13, 6] # BCM numbering
COL_PINS = [21, 20, 16, 12] # BCM numbering

factory = rpi_gpio.KeypadFactory()

# Try factory.create_4_by_3_keypad
# and factory.create_4_by_4_keypad for reasonable defaults
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)



keyboard = Controller()


#button controller with timed led to show button press    
    
def printKey(key):
  print(key)
  if (key=="A"):
    with keyboard.pressed(Key.ctrl):
        keyboard.press('j')
        keyboard.release('j')
    on(r4)
    s(.1)
    off(r4)
    
  if (key=="B"):
    with keyboard.pressed(Key.ctrl):
        keyboard.press('b')
        keyboard.release('b')
    on(r4)
    s(.1)
    off(r4)
        
  if (key=="C"):
    with keyboard.pressed(Key.ctrl):
    
        keyboard.press('r')
        keyboard.release('r')
        on(r4)
        s(.1)
        off(r4)
        
  if (key=="D"):
    with keyboard.pressed(Key.ctrl):
        keyboard.press('f')
        keyboard.release('f')
        on(r4)
        s(.1)
        off(r4)    
    
    
  if (key=="1"):
    with keyboard.pressed(Key.ctrl):
        keyboard.press('d')
        keyboard.release('d')
    on(r4)
    s(.1)
    off(r4)
    s(.2)
    
  if (key=="2"):
    
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    on(r4)
    s(.1)
    off(r4) 
    
  if (key=="3"):
    
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    on(r4)
    s(.1)
    off(r4)
    
  if (key=="4"):
    
    keyboard.press(Key.f11)
    keyboard.release(Key.f11)
    on(r4)
    s(.1)
    off(r4)


    
    

  if (key=="E"):
    with keyboard.pressed(Key.shift):
        with keyboard.pressed(Key.ctrl):
            keyboard.press('b')
            keyboard.release('b')
            on(r4)
            s(.1)
            off(r4)
            s(.2)
            
  if (key=="F"):
     with keyboard.pressed(Key.ctrl):
        keyboard.press('a')
        keyboard.release('a')
        on(r4)
        s(.1)
        off(r4)
        s(.2)

            
  if (key=="G"):
    with keyboard.pressed(Key.ctrl):
    
        keyboard.press('t')
        keyboard.release('t')
        on(r4)
        s(.1)
        off(r4)
        
  if (key=="H"):
    with keyboard.pressed(Key.ctrl):
            
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        on(r4)
        s(.1)
        off(r4)
        
  if (key=="5"):
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        on(r4)
        s(.1)
        off(r4)
        
        
  if (key=="6"):
    with keyboard.pressed(Key.ctrl):
        on(r4)
        s(.1)
        off(r4)

  if (key=="7"):
    with keyboard.pressed(Key.ctrl):
	keyboard.press('q')
        keyboard.release('q')
        on(r4)
        s(.1)
        off(r4)
        
  if (key=="8"):
    with keyboard.pressed(Key.ctrl):      
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        on(r4)
        s(.1)
        off(r4)
        
        
#led 
g1 = 7
g2 = 9
g3 = 10
g4 = 2
r1 = 8
r2 = 11
r3= 22
r4 = 3
g5 = 18
r5= 15
s = time.sleep

GPIO.setup(g1, GPIO.OUT)
GPIO.setup(g2, GPIO.OUT)
GPIO.setup(g3, GPIO.OUT)
GPIO.setup(g4, GPIO.OUT)
GPIO.setup(r1, GPIO.OUT)
GPIO.setup(r2, GPIO.OUT)
GPIO.setup(r3, GPIO.OUT)
GPIO.setup(r4, GPIO.OUT)
GPIO.setup(r5, GPIO.OUT)    
GPIO.setup(g5, GPIO.OUT)
def on(led):
    GPIO.output(led, True)

def off(led):
    GPIO.output(led, False)





# printKey will be called each time a keypad button is pressed
keypad.registerKeyPressHandler(printKey)

try:
  while(True):
    time.sleep(0.2)
except:
 keypad.cleanup()