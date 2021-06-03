import json
import socket
from logic.utils.qr import Qr
from werkzeug.serving import make_server
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import argparse
from logic.automations.playback_control import PlaybackControl
from logic.utils.systemInfo import SystemInfo

app = Flask(__name__)
app.config["ENV"] = "development"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["active"] = True
db = SQLAlchemy(app)


@app.route('/')
def home():
    # print(SystemInfo().minimalInfo())
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


@app.route('/exit', methods=["GET"])
def exit_app():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return "Server shutting down"


def start_server(host):
    app.run(host=host)


if __name__ == '__main__':
    ips = socket.gethostbyname_ex(socket.gethostname())[-1]
    if type(ips) == list:
        print("choose the specified ip")
        for i in range(len(ips)):
            print(str(i+1)+") "+ips[i])
        indexIP = int(input())
        ip = ips[indexIP-1]
    else:
        ip = ips
    qrData = SystemInfo().qrInfo(ip)
    Qr(str(qrData)).generate()
    # start server
    start_server(ip)
