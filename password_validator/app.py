from flask import Flask, render_template, request, redirect, url_for, jsonify
import re

app = Flask(__name__)

def validate_password(password):
    messages = []

    if len(password) < 8:
        messages.append("Password is too short. It must be at least 8 characters long.")
    if not re.search(r"[A-Z]", password):
        messages.append("Password must contain at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        messages.append("Password must contain at least one lowercase letter.")
    if not re.search(r"\d", password):
        messages.append("Password must contain at least one number.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        messages.append("Password must contain at least one special character.")

    return messages

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def validate_username(username):
    pattern = r"^[a-zA-Z0-9]{5,15}$"
    return re.match(pattern, username) is not None

def validate_psswd(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$"
    return re.match(pattern, password) is not None


@app.route('/', methods=['GET', 'POST'])
def index():
    username_valid = None
    password_valid = None
    email_valid = None
    show_register = False

    if request.method == 'POST':
        if 'register' in request.form:
            show_register = True
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            username_valid = validate_username(username)
            password_valid = validate_psswd(password)
            email_valid = validate_email(email)
            if username_valid and password_valid and email_valid:
                return redirect(url_for('welcome'))

    return render_template('index.html', username_valid=username_valid, password_valid=password_valid, email_valid=email_valid, show_register=show_register)

@app.route('/validate_password', methods=['POST'])
def validate_password_route():
    password = request.json.get('password')
    validation_messages = validate_password(password)
    return jsonify({'messages': validation_messages})

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)
