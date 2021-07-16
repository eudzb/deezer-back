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

@app.route('/topArtist')
@cross_origin() # allow all origins all methods.
def topArtist():

    topArtists = requests.get(URL_API + "/chart/0/artists")
    json_artists = topArtists.json()
    return json_artists

@app.route('/artist')
@cross_origin() # allow all origins all methods.
def idArtist():

    id = request.args.get('id')
    idArtist = requests.get(URL_API + "/artist/" + id)
    json_artist = idArtist.json()
    return json_artist 

@app.route('/artistRelated')
@cross_origin() # allow all origins all methods.
def artisrRelated():

    id = request.args.get('id')
    artistRelated = requests.get(URL_API + "/artist/" + id + "/related?limit=5")
    json_artist_related = artistRelated.json()
    return json_artist_related

@app.route('/artistTopTrack')
@cross_origin() # allow all origins all methods.
def artistTopTrack():

    id = request.args.get('id')
    artistTopTrack = requests.get(URL_API + "/artist/" + id + "/top")
    json_artist_top_track = artistTopTrack.json()
    return json_artist_top_track

@app.route('/genreArtist')
@cross_origin() # allow all origins all methods.
def genreArtist():

    id = request.args.get('id')
    genreArtist = requests.get(URL_API + "/genre/" + id + "/artists?limit=15")
    json_genre_artist = genreArtist.json()
    return json_genre_artist

@app.route('/genrePodcast')
@cross_origin() # allow all origins all methods.
def genrePodcast():

    id = request.args.get('id')
    genrePodcast = requests.get(URL_API + "/genre/" + id + "/podcasts?limit=15")
    json_genre_podcast = genrePodcast.json()
    return json_genre_podcast

@app.route('/genreRadios')
@cross_origin() # allow all origins all methods.
def genreRadios():

    id = request.args.get('id')
    genreRadios = requests.get(URL_API + "/genre/" + id + "/radios?limit=15")
    json_genre_radios = genreRadios.json()
    return json_genre_radios

if __name__=='__main__':
    app.run()
