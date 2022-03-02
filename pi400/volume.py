from RPi import GPIO
from time import sleep
import time
import alsaaudio
import Encoder
from pynput.mouse import Button, Controller

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Change the following pins based on your application or HAT in use
#volume
encoder_clk = 4
encoder_data = 17
encoder_button = 14
scroll_button = 5
r4 = 3
s = time.sleep

def on(led):
    GPIO.output(led, True)

def off(led):
    GPIO.output(led, False)

#Scroll Wheel




GPIO.setup(encoder_clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(encoder_data, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(encoder_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

m = alsaaudio.Mixer()
mouse = Controller()

                    

#Volume Control



# Set desired minimum and maximum values
min = 0
max = 100

# Set the volume change step size
volume_step_size=3

is_Muted = m.getmute()[0]
volume = m.getvolume()[0]

if is_Muted == 0:
    is_Muted=False
else:
    is_Muted=True
clkLastState = GPIO.input(encoder_clk)
btnLastState = GPIO.input(encoder_button)

try:
    while True:
        btnPushed = GPIO.input(encoder_button)
        if ((not btnLastState) and btnPushed):
            if is_Muted:
                is_Muted = False
                m.setmute(0)
                GPIO.output (15, False)
                GPIO.output (18, True)
            else:
                is_Muted = True
                m.setmute(1)
                GPIO.output (15, True)
                GPIO.output (18, False)
                sleep(0.05)
        else:
            clkState = GPIO.input(encoder_clk)
            dtState = GPIO.input(encoder_data)
            if clkState != clkLastState:
                if dtState != clkState:
                    volume += volume_step_size/2
                    if volume > max:
                        volume = max
                else:
                    volume -= volume_step_size/2
                    if volume < min:
                        volume = min
                if clkState == 1:
                                        m.setvolume(int(volume))
            clkLastState = clkState
        btnLastState = btnPushed

finally:
    GPIO.cleanup()