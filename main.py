# NESNAS v1
# Dean Ralph
# Jan 2020

# Description:
# Basic NAS interface with a NES theme

#Imports
from flask import Flask, render_template, request

#Main App
app = Flask(__name__)

login = False

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'GET':
        if login:
            return render_template("index.html")
        else:
            return render_template("login.html")

# @app.route('/settings', methods = ['POST', 'GET'])
# def dbsettings():
#     if request.method == 'POST':
#         dbresult = request.form
#         with open('dbconfig.json', 'w') as outfile:
#             json.dump(dbresult, outfile, indent=2)
#         return "Settings Saved"
#     if request.method == 'GET':
#         sqlConf = loadConfig('dbconfig.json')
#         return render_template('settings.html', servervalue=sqlConf["server"], dbvalue=sqlConf["database"], uservalue=sqlConf["username"])

if __name__ == "__main__":
    app.run()