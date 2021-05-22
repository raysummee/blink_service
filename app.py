import json
import re
from werkzeug.serving import make_server
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import argparse
from logic.automations.playback_control import PlaybackControl

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


def ip_address(arg_value):
    pat = re.compile(
        r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$")
    if not pat.match(arg_value):
        raise TypeError
    return arg_value


if __name__ == '__main__':
    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("ip", type=ip_address, help="The pc's ip address")

    # Read arguments from command line
    args = parser.parse_args()

    # start server
    start_server(args.ip)
