#!/usr/bin/env python3

import serial
import tkinter as tk
from tkinter import ttk

# Define the serial port and baud rate
SERIAL_PORT = '/dev/ttyACM0'
BAUD_RATE = 9600

# Create a serial object and reset the input buffer
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
ser.reset_input_buffer()

# Create a Tkinter window
root = tk.Tk()
root.title('Send Number to Arduino')

# Create a default value for the slider
default_value = 0

# Define a function to send the selected value to the Arduino
def send_number(*args):
    # Get the selected value from the slider
    value = int(slider.get())

    # Send the value to the Arduino
    ser.write(str(value).encode('utf-8'))
    print("Sent value to Arduino:", value)

# Create a slider widget and set its range and default value
slider = ttk.Scale(root, from_=0, to=255, orient='horizontal')
slider.set(default_value)
slider.pack()

# Call the send_number function whenever the slider value is changed
slider.bind("<ButtonRelease-1>", send_number)

# Send the default value to the Arduino when the application starts
ser.write(str(default_value).encode('utf-8'))

# Start the Tkinter main loop
root.mainloop()
