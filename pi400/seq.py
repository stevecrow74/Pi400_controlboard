#welcome
import time
import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


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
    
on(g1)
s(.2)
on(g2)
s(.2)
on(g3)
s(.2)
on(g4)
s(2)
off(g1)
s(.1)
on(r1)
s(.1)
off(g2)
s(.1)
on(r2)
s(.1)
off(g3)
s(.1)
on(r3)
s(.1)
off(g4)
s(.1)
on(r4)
s(1)
on(r5)
s(1)
off(r5)
on(g5)
s(1)
off(r1)
off(r2)
off(r3)
off(r4)
off(g5)
s(.5)
on(g5)
s(.1)

import rotary
