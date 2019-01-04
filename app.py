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
  password = request.form['password']
  username = request.form['username']

  user_exists = query_db('SELECT COUNT(*) FROM USERS WHERE username = ?', [username])

  if(user_exists[0][0] == 1):
    password_true = query_db('SELECT COUNT(*) FROM USERS WHERE username = ? AND password = ?', (username, password))
    if(password_true[0][0] == 1):
      session['login'] = "username"
      return "You have logged in. Welcome Steven."
    else:
      flash('Invalid login. This attempt has been logged.')
      return redirect(url_for('verifyuser'))
  else:
    flash('Login failed.')
    return redirect(url_for('verifyuser'))



#-----------------------------------------------------------------
# Error handlers for malicious users, accidents, and bots.
# -----------------------------------------------------------------

@app.route('/config')
def submit():
  return redirect("https://www.fbi.gov/", code=302)

@app.errorhandler(400)
def error(e):
  return render_template('error.html'), 400

@app.errorhandler(401)
def error(e):
  return render_template('error.html'), 401

@app.errorhandler(403)
def error(e):
  return render_template('error.html'), 403

@app.errorhandler(404)
def error(e):
  return render_template('error.html', code=404), 404





#-----------------------------------------------------------------
# connection_to_sqlite_database as the name implies handles our
# connection to the SQLITE database.db database file. We keep
# the connection open until our database commits/reads have 
# fully completed. 
# -----------------------------------------------------------------

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
  
def isLoggedIn():
  if(session.get('login') is None):
    return False
  else:
    return True


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug=True)
