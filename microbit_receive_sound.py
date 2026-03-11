# microbit_receive_sound.py
# This MicroPython program runs on the micro:bit.
# It listens for a number sent via serial and plays a sound.

from microbit import *
import music

while True:
    
    if uart.any():  # check if data received
        
        data = uart.readline().strip()
        
        number = int(data)
        
        display.show(number)
        
        # play sound when number received
        music.play(music.BA_DING)
