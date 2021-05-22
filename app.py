import json

import pyautogui
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from logic.automations.playback_control import PlaybackControl
from logic.utils.systemInfo import SystemInfo

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
app.config["active"] = True
db = SQLAlchemy(app)


@app.route('/')
def home():
    print(SystemInfo().minimalInfo())
    return render_template('home.html')


@app.route('/activate/<to>', methods=["POST"])
def activate(to: bool):
    if not app.config["active"] == to:
        app.config["active"] = to


@app.route('/activate', methods=["GET"])
def activate_view():
    return json.dumps({"active": app.config["active"]})


@app.route('/playback/<command>', methods=["GET"])
def playback(command):
    try:
        getattr(PlaybackControl(), command)()
    except AttributeError:
        return "error"
    return "done"


if __name__ == '__main__':
    app.run()
