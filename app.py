from pytube import YouTube
from pytube.cli import on_progress

link = 'https://www.youtube.com/watch?v=_4_Iwg17ehs'
yt = YouTube(link)

print('\n', yt.streams.order_by('resolution').desc().first())
#steam.download(output_path='/Users/hara/Desktop/DL')