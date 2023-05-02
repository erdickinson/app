# Importing the required modules
from flask import Flask, render_template
import os
import serial

# Initializing the Flask app
app = Flask(__name__)

# Initializing the serial port
ser = serial.Serial('/dev/ttyACM0', 9600)
value = 0

# Defining the routes
@app.route("/")
def index():
    return render_template("index.html", value=value)

@app.route("/decrease_20")
def decrease_20():
    global value
    if value - 20 >= 0:
        value -= 20
    ser.write(str(value).encode() + b'\n')
    return str(value)

@app.route("/decrease_10")
def decrease_10():
    global value
    if value - 10 >= 0:
        value -= 10
    ser.write(str(value).encode() + b'\n')
    return str(value)

@app.route("/increase_10")
def increase_10():
    global value
    if value + 10 <= 100:
        value += 10
    ser.write(str(value).encode() + b'\n')
    return str(value)

@app.route("/increase_20")
def increase_20():
    global value
    if value + 20 <= 100:
        value += 20
    ser.write(str(value).encode() + b'\n')
    return str(value)

# Running the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
