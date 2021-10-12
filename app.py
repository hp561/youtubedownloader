from flask.wrappers import Response
from pytube import YouTube
from flask import Flask
from flask import request
import ffmpeg
import os
import time
from flask import send_from_directory

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the YT downloader v1"

@app.route('/download', methods=["POST"])
def download_video():
    link = request.get_json()

    try:
        url = link.get('link', 'https://www.youtube.com/watch?v=23sp3cj5Pnc')
        yt = YouTube(url)

        #Title of video
        print("Title: "+yt.title)#Number of views of video
        print("Number of views: ",yt.views)#Length of the video
        print("Length of video: ",yt.length,"seconds")#Description of video
        print("Description: ",yt.description)#Rating
        print("Ratings: ",yt.rating)

        print("Downloading...")
        # audio_stream = yt.streams.filter(only_audio=True)[0].download(filename='audio.mp4')
        ys = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename='video.mp4')
        # video_stream = ffmpeg.input('video.mp4')
        # audio_stream = ffmpeg.input('audio.mp4')
        # ffmpeg.concat(video_stream, audio_stream, v=1, a=1).output('inished_video.mp4').run()
        print("Download completed!!")
        return send_from_directory('/Users/harsh/Documents/python', 'video.mp4', as_attachment=True)
    except Exception as e:
        return str(e)



if __name__ == '__main__':
    app.run(debug=True)

