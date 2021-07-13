from flask import Flask, render_template, request, session, logging, url_for, redirect, flash
import requests, json, datetime, random, os
from werkzeug.utils import secure_filename
from time import *

# Instancier notre application dont le nom est __main__
app = Flask(__name__)

@app.route('/')
def home():

    genres = requests.get("https://api.deezer.com/genre")
    json_genres = genres.json()
    return json_genres

if __name__=='__main__':
    app.run()
