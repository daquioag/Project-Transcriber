import urllib.parse
from urllib import parse
from urllib.parse import parse_qs
from contextlib import suppress
from flask import Flask, jsonify
from flask import request # used to parse payload
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from flask import render_template
from flask import abort
from extraction import convert_URL_to_ID
import datetime

# define a variable to hold you app
app = Flask(__name__)

# # define your resource endpoints
# @app.route('/')
# def index_page():
#     ed_test = convert_URL_to_ID("https://www.youtube.com/watch?v=_dK2tDK9grQ")
#     transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

#     return transcript_list


# # server the app when this file is run
# if __name__ == '__main__':
#     app.run(debug=True)


# define your resource endpoints
@app.route('/')
def index_page():
    return "Hello world"

@app.route('/time', methods=['GET'])
def get_time():
    return str(datetime.datetime.now())

# server the app when this file is run
if __name__ == '__main__':
    app.run(debug=True)