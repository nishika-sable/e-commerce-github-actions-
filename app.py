from flask import Flask, render_template
AWS_ACCESS_KEY_ID = "REDACTED"
app = Flask (__name__)
@app.route ('/')
def home():
    return  render_template('index.html')
    