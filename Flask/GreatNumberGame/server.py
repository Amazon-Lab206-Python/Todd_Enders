from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.secret_key = "secretsauce"

@app.route("/")
def index():
    try:
        session['winner']
    except:
        session['winner'] = random.randint(1,100)

    return render_template('index.html')

@app.route('/guess', methods=["POST"])
def guess():
    # print type(request.form['guess'])
    if (int(request.form['guess']) == session['winner']):
        print "You win"
        session['result'] = "win"
    elif (int(request.form['guess']) > session['winner']):
        print "too high"
        session['result'] = "high"
    else:
        print "too low"
        session['result'] = "low"

    return redirect('/')

@app.route('/replay', methods=["POST"])
def replay():
    session.clear()
    return redirect('/')

app.run(debug=True)