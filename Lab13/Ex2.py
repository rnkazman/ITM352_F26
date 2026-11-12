# Application that allows a user to login.  If login credentials are correct,
# the user is welcomed.  If not, an error message is displayed.
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userid = request.form['username']
        password = request.form['password']
        # Replace this with your actual authentication logic
        if USERS.get(userid) == password:
            return redirect(url_for('success', username=userid))
        else:
            return "Sorry bud.  Try again."
    else:
        return render_template('login.html')

@app.route('/success/<username>')
def success(username):
    return render_template('success.html', username=username)

USERS = {"port": "port123",
        "kazman": "kazman123"}


if __name__ == '__main__':
    app.run(debug=True)