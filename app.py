from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():
    num = request.form['number']
    # Send the number to the Arduino
    return render_template('index.html', message='Number sent to Arduino!')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
