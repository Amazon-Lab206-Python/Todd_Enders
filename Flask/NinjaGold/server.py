from flask import Flask, render_template, redirect, session, request 
app = Flask(__name__)
app.secret_key = "spaceghost"
import random 
import datetime

@app.route('/')
def index():
    try:
        session['gold']
        session['activities']
    except:
        session['gold'] = 0
        session['activities'] = []

    return render_template('index.html')

@app.route('/process_money', methods=["POST"])
def process_money():
    building = request.form['building']

    if building == 'farm':
        gold = random.randint(10,20)
        session['gold'] += gold 
        activity = ("win","You entered a {} and earned {} golds ({})".format(building, gold, datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')))
        session['activities'].append(activity)
    
    elif building == 'cave':
        gold = random.randint(5,10)
        session['gold'] += gold 
        activity = ("win","You entered a {} and earned {} golds ({})".format(building, gold, datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')))
        session['activities'].append(activity)
    
    elif building == 'house':
        gold = random.randint(2,5)
        session['gold'] += gold 
        activity = ("win","You entered a {} and earned {} golds ({})".format(building, gold, datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')))
        session['activities'].append(activity)
    
    elif building == 'casino':
        gold = random.randint(-50,50)
        session['gold'] += gold 
        if (gold >= 0):
            activity = ("win","You entered a {} and earned {} golds ({})".format(building, gold, datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')))
        else:
            activity = ("lose","You entered a {} and lost {} golds ({})".format(building, gold*-1, datetime.datetime.now().strftime('%Y/%m/%d %I:%M %p')))
        
        session['activities'].append(activity)

    return redirect('/')

@app.route('/reset')
def reset_game():
    session.clear()
    return redirect('/')

app.run(debug=True)