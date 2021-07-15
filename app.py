from flask import Flask, render_template, request, session, logging, url_for, redirect, flash
import requests, json, datetime, random, os
import logging
from werkzeug.utils import secure_filename
from time import *
from flask_cors import CORS, cross_origin

# Instancier notre application dont le nom est __main__
app = Flask(__name__)
CORS(app)
URL_API = "https://api.deezer.com"

@app.route('/')
@cross_origin() # allow all origins all methods.
def home():

    genres = requests.get(URL_API + "/genre")
    json_genres = genres.json()
    return json_genres

@app.route('/topAlbum')
@cross_origin() # allow all origins all methods.
def topAlbum():

    albums = requests.get(URL_API + "/chart/0/albums?limit=10")
    json_albums = albums.json()
    return json_albums

@app.route('/album')
@cross_origin() # allow all origins all methods.
def idAlbum():

    id = request.args.get('id')
    idAlbums = requests.get(URL_API + "/album/" + id)
    json_album = idAlbums.json()
    return json_album 

if __name__=='__main__':
    app.run()
