from flask import Flask, render_template, request
from flask.json import jsonify
from models.models import *
import json

with open("data/data.json", "r") as f:
    playlists_file = json.load(f)

playlists = ListOfLibraries()
playlists.fill_from_dict(playlists_file)

app = Flask("reproductor-musica")

@app.route("/")
def main():
    return render_template("base.html")

@app.route("/data", methods=("GET", "POST"))
def data():
    if request.method == "GET":
        return jsonify(playlists.to_dict())
    if request.method == "POST":
        data = json.loads(request.get_data())
        execute_instruction(data[0], data[1], playlists)
        return jsonify(playlists.to_dict())