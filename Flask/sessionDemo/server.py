from flask import Flask, render_template, request, session, redirect 
app = Flask(__name__)
app.secret_key = "this is so secret"

@app.route('/')
def index():
    # if not 'counter' in session:
    #     session['counter'] = 0
    
    try:
        session['counter']
    except:
        session['counter'] = 0

    return render_template('index.html')


@app.route('/info', methods=["POST"])
def info():
    # session['first_name'] = request.form['first_name']
    # session['last_name'] = request.form['last_name']
    # session['email'] = request.form['email']
    session['counter'] += 1

    session['form_data'] = request.form
    print session['form_data']['user_id']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')


app.run(debug=True)