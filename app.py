from flask import Flask, render_template, request, session, logging, url_for, redirect, flash
import requests, json, datetime, random, os
from werkzeug.utils import secure_filename
from time import *
from flask_cors import CORS, cross_origin

# Instancier notre application dont le nom est __main__
app = Flask(__name__)
CORS(app)

@app.route('/')
@cross_origin() # allow all origins all methods.
def home():

    genres = requests.get("https://api.deezer.com/genre")
    json_genres = genres.json()
    return json_genres

if __name__=='__main__':
    app.run()
