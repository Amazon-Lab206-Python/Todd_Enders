from flask import Flask, render_template, request 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/result', methods=["post"])
def info():
    print request.form['first_name']
    print request.form['last_name']
    pass

app.run(debug=True)