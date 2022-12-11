from flask import Flask, render_template, url_for

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def dashboard():
    return render_template('index.html')

@app.route("/diagnosa")
def diagnosa():
    return render_template('diagnosa.html')

@app.route("/history")
def history():
    return render_template('history.html')