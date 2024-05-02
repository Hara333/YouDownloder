from pytube import YouTube
from pytube.cli import on_progress

link = 'https://www.youtube.com/watch?v=_4_Iwg17ehs'
yt = YouTube(link, on_progress_callback=on_progress())
print('\n', yt.streams.filter(res='720p'))
steam = yt.streams.get_by_itag(22)
steam.download(output_path="/Users/hara/Desktop/DL")