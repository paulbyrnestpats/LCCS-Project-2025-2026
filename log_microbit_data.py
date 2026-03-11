# log_microbit_data.py
# This script reads data from the micro:bit using serial communication
# and saves it into a CSV file.

import serial
import csv

ser = serial.Serial('COM3', 115200)

with open("sensor_data.csv", "a", newline="") as file:
    writer = csv.writer(file)

    while True:
        data = ser.readline().decode().strip()
        print(data)

        writer.writerow([data])
