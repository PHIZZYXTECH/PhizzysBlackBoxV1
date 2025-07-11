from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # from blackbox import simulate_hack  # Temporarily disabled for Render startup
    # simulate_hack()

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
