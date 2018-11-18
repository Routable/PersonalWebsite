import sqlite3 
from flask import Flask, request, render_template, redirect, url_for, session, flash, g, abort


app = Flask(__name__)
DATABASE = 'database.db'
app.secret_key = '12308adsijkadsads129033210321'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/verifyuser')
def verifyuser():
  browser_ip = request.remote_addr
  return render_template('verifyuser.html', browser_ip = browser_ip)

@app.route('/authenticate_user', methods=['POST'])
def authenticate_user():
  if request.form['username'] == 'sbucholtz' and request.form['password'] == 'password':
    return "pls stop"
  else:
    flash('Invalid login. This attempt has been logged.')
    return redirect(url_for('verifyuser'))



@app.route('/submit')
def submit():
  return 'stop it'

@app.errorhandler(418)
def foureighteen(e):
  return render_template('418.html'), 418


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug=True)
