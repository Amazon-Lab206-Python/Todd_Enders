from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def no_ninjas():
    return render_template('noninjas.html')

@app.route('/ninja')
def all_ninjas():
    return render_template('allninjas.html')

@app.route('/ninja/<color>')
def one_ninja(color):
    turtles = {
        'blue': 'leonardo',
        'purple': 'donatello',
        'red': 'raphael',
        'orange': 'michelangelo',
    }
    if color not in turtles:
        selected = 'notapril'
    else:
        selected = turtles[color]
    
    return render_template('oneninja.html', image=selected)

app.run(debug=True)