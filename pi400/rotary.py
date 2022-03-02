import RPi.GPIO as GPIO
from pynput.mouse import Button, Controller
from time import sleep
GPIO.setwarnings(False)
mouse = Controller()

#ctl and data pin GPIO
pin_a = 24 
pin_b = 25


GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_b, GPIO.IN, pull_up_down=GPIO.PUD_UP)

device = mouse.scroll
seq_a = seq_b = 0



        
#scroll function

def on_edge(pin):
    global seq_a, seq_b
    a = GPIO.input(pin_a)
    b = GPIO.input(pin_b)
    seq_a = ((seq_a << 1) | a) & 0b1111
    seq_b = ((seq_b << 1) | b) & 0b1111
    if seq_a == 0b0011 and seq_b == 0b1001:
        device(0,1)
    elif seq_a == 0b1001 and seq_b == 0b0011:
        device(0,-1)

GPIO.add_event_detect(pin_a, GPIO.BOTH, callback=on_edge)
GPIO.add_event_detect(pin_b, GPIO.BOTH, callback=on_edge)

try:
    while True:
        sleep(3600)
except KeyboardInterrupt:
    print("...DONE")
    GPIO.cleanup()