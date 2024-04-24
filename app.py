from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Mock user data (replace with your actual user authentication logic)
users = {'Lavanya': 'Lavpassword'}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # If login successful, redirect to main page
        return redirect(url_for('main_page'))
    else:
        # If login fails, redirect back to login page
        return redirect(url_for('index'))

@app.route('/main_page')
def main_page():
    # Render the main page template
    return render_template('main_page.html')

@app.route('/attendance')
def attendance():
    return render_template('attendance.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/backup')
def backup():
    return render_template('backup.html')

if __name__ == '__main__':
    app.run(debug=True)
