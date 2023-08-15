from flask import Flask,render_template
import data as d

app = Flask(__name__,template_folder="static_files",static_folder="templates")

@app.route("/")
def mainpage():
    return render_template("main.html")

@app.route("/imax")
def imax():
    print("imax")
    text = d.imax_data_rev()
    return render_template("imax.html",data = text)