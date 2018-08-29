import os
from pytube import YouTube
path = os.getcwd()
link = input("Enter the link")
YouTube(link).streams.first().download(path)