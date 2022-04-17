from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, jsonify, session
from flask_session import Session

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOADED"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///users.db")

@app.route("/")
def login():
        return render_template("login2.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

