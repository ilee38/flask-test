from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sim')
def simulation():
    return render_template('sim.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
