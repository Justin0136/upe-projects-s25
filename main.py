from flask import Flask, render_template
import time, math

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')