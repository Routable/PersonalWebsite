#!/usr/bin/env python3

import sqlite3 
from flask import Flask, request, render_template, redirect, url_for, session, flash, g, abort

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')


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


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug=True)
