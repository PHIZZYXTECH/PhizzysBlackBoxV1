from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    os.system("clear")
    from blackbox import simulate_hack
    simulate_hack()
    app.run(debug=True)
