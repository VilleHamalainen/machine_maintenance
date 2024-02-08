from flask import Flask, jsonify, render_template, request
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


@app.route('/student')
def student_form():
    # implement login?
    return render_template('studentform.html')

@app.route('/admin')
def admin_form():
    # implement login
    return render_template('adminform.html')


@app.route('/submit', methods = ['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    return f"Hello {name}, your email is {email}."



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
