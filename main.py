# NESNAS v1
# Dean Ralph
# Jan 2020

# Description:
# Basic NAS interface with a NES theme

#Imports
from flask import Flask, render_template, request
import drive

#Main App
app = Flask(__name__)

login = False
noOfDrives = drive.noOfDisks()

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        login = request.form
        with open('config.txt', 'w') as outfile:
            outfile.write(login)
        return "Settings Saved"
    if request.method == 'GET':
        if login:
            return render_template("index.html")
        else:
            return render_template("login.html")

if __name__ == "__main__":
    app.run()