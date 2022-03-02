# Pi400_controlboard

A simple control board  for a raspberry pi400,<br>
16 button matrix keypad<br>
2 rotary encoders<br>
5 dual red/green led's<br>
<p>
 <b>Volume.py</b><br>
  a simple script that uses one of the rotary encoders as a volume control and mute switch, with dual red/green led <br>
  this is coded for a standard rotary encoder with 5 pins, SW, GND, CTL,GND, DT.<br>
  <p>
    <b>buttons.py</b><br>
    coded for a self built 16 button matrix keypad, but could be used for other keypads.<br>
    this is coded specifically to be used with GQRX as a shortcut keypad.<br>
    when a button is pressed it sends the code as well as flashing one of the led's red to confirm key press.<br>
    <p>
      <b> rotary.py</b><br>
      this uses the second rotary encoder to be used as a scroll wheel, the button isnt yet programmed.<br>
      <p>
        <b> seq.py</b><br>
        just a little script to test all leds are working.<br>
       <p>
        <b> load.sh</b><br>
        an executable bash file that runs volume.py, buttons.py and rotary.py together.<br>
        I might clean up the code into one file at some stage.
      
                                                                                                           
  
