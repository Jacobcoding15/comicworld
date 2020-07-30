# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import get_info
from datetime import datetime
# -- Initialization section --
app = Flask(__name__)
# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', time=datetime.now())
@app.route('/results', methods=['GET', 'POST'])
def results():
    print(request.form)
    user_name=(request.form["character_name"])
    
    info = get_info(user_name)
    return render_template("results.html", user_name=user_name, info=info, time=datetime.now())