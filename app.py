from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def show_home_route():
  return "Home Route working..."
