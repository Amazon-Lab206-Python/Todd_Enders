from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "secret_squirrel"

@app.route("/")
def index():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 1
    return render_template('index.html')

app.run(debug=True)