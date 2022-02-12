import functools
import python.code.utils.extractor
import python.code.utils.music_finder
from python.code.utils.music_finder import MusicFinder
from python.code.utils.extractor import Data
import python.code.config as config
import os
from python.code.rec import *
from python.code.git import *


def final(rand_filename):
    gitupload(rand_filename)
    #requesting the api
    os.environ['api_token'] = 'Your Api Key'
    config.SPOTIFY = True
    url_name = 'repolink'+rand_filename+'.m4a?raw=true'
    music = MusicFinder('True',url_name)
    audio_data = Data(music.finder())

    class final:
        type: str
        Title: str
        ArtistName: str
        Album: str
        Label: str
        ReleaseDate: str
        Link: str
        img: str

    output = final()

    if (audio_data.result() == None):
        output.type = "no"
    else:
        output.type = "yes"

    output.Title = audio_data.title()
    output.ArtistName = audio_data.artist()
    output.Album = audio_data.album()
    output.Label = audio_data.label()
    output.ReleaseDate = audio_data.release_date()
    output.Link = audio_data.SPOTIFY_spotify()
    output.img = audio_data.SPOTIFY_img()
    print("done")
    return output
