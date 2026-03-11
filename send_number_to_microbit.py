# send_number_to_microbit.py
# This Python script sends a number to a micro:bit over serial.
# The micro:bit will receive the number and trigger a sound.

import serial
import time

# Replace COM3 with your micro:bit port
ser = serial.Serial('COM3', 115200)

time.sleep(2)  # wait for connection to establish

number = input("Enter a number to send to micro:bit: ")

# Send number with newline
ser.write((number + "\n").encode())

print("Number sent to micro:bit:", number)

ser.close()
