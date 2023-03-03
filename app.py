from flask import Flask, render_template, request
import serial

app = Flask(__name__)

# Define the serial port and baud rate
SERIAL_PORT = '/dev/ttyACM0'
BAUD_RATE = 9600

# Create a serial object and reset the input buffer
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
ser.reset_input_buffer()

# Define the route for the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    # If the form was submitted, read the slider value and send it to the Arduino
    if request.method == 'POST':
        value = int(request.form['slider'])
        ser.write(str(value).encode('utf-8'))
        print("Sent value to Arduino:", value)

    # Render the template without a default value for the slider
    return render_template('index.html')

if __name__ == '__main__':
    # Start the Flask server
    app.run(debug=True, host='0.0.0.0')
