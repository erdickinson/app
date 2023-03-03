from flask import Flask, render_template
import os
import serial

app = Flask(__name__)

ser = serial.Serial('/dev/ttyACM0', 9600)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<value>")
def set_value(value):
    ser.write(value.encode())
    return "Value sent: " + value

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
