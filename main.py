from flask import Flask, jsonify, render_template, request
import os
from models.maintenance_repository import Machine, User, db

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///maintenace.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.init_app(app)

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
def submit_user_data():
    name = request.form.get('name')
    email = request.form.get('email')
    return f"Hello {name}, your email is {email}."

@app.route('/machine_data', methods = ['POST'])
def submit_machine_data():
    id = request.form.get('id')
    name = request.form.get('machinename')
    run_time = request.form.get('runtime')
    fuel_amount = request.form.get('fuelamount')
    return f"Machine {id}, {name}, {run_time}, {fuel_amount}."


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
