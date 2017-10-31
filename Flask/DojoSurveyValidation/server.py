from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "using_flash_requires_secret_key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=["POST"])
def result():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    errors = False
    if len(name) == 0:
        errors = True
        flash('Name cannot be blank')
    if len(comment) == 0:
        errors = True        
        flash('Comment cannot be blank')
    elif len(comment) > 120:
        errors = True 
        flash('Comment cannot have more than 120 characters')
        
    if errors:
        return redirect('/')
    
    return render_template('result.html', name=name, location=location, language=language, comment=comment)

app.run(debug=True)