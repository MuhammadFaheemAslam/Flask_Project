"""
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    greeting = ""
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            greeting = f"Hello, {name}!"
    return render_template('index.html', greeting=greeting)
"""

from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'  

@app.route('/', methods=['GET', 'POST'])
def home():
    greeting = ""
    if request.method == 'POST' and 'name' in request.form:
        name = request.form['name']
        greeting = f"Hello, {name}! Welcome to our site."
        flash(greeting)
        return redirect(url_for('home'))
    return render_template('index.html')


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST' and 'comment' in request.form:
        comment = request.form['comment']
        message = f"Thank you for your feedback: {comment}"
        flash(message)
        return redirect(url_for('feedback'))
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
#github 
#https://github.com/MuhammadFaheemAslam/Flask_Project