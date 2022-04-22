#!/usr/bin/env python3

from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Hello, World!'

@app.route('/') # main url
def index():
  return render_template("subscriber.html")

host = '0.0.0.0'
port = '9900'

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
    