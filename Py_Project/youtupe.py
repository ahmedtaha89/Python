# pip install pytube3
from pytube import YouTube 
url = input("Enter URL: ")
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download()