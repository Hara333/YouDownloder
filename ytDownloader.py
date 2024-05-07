import customtkinter as ctk
from pytube import YouTube
from PIL import Image, ImageTk
import requests
import datetime

window = ctk.CTk()
window.geometry('720x720')
window.title('YouTube Downloader')

width = 360
height = 200

def on_progress(steam, chunk, byte_remaining):
    total_size = steam.filesize
    byte_downloaded = total_size - byte_remaining
    percen_dl = byte_downloaded / total_size * 100
    per = int(percen_dl)
    print(per/100)
    dl_progress.set(per)
    percen_label.configure(text=str(per) +" %")
    percen_label.update()
def clicker():
    link = url_entry.get()
    yt = YouTube(link, on_progress_callback=on_progress)

    global steam_mp3
    global steam_mp4
    info_label.configure(text=yt.title)
    duration_label.configure(text="Duration: " + str(datetime.timedelta(seconds=yt.length)))
    label_image.configure(image=image_thumbnail, width=width, height=height)
    image_thumbnail.configure(light_image=Image.open(requests.get(yt.thumbnail_url,stream=True).raw),size=(width,height))

    steam_mp3 = yt.streams.filter(only_audio=True).desc().first()
    btn_mp3.configure(text=str(steam_mp3)[47:55].replace('"','') + " | " + str(steam_mp3.filesize_mb) +" MB")
    label_mp3.pack()
    btn_mp3.pack()

    steam_mp4 = yt.streams.filter(res='720p').desc().first()
    btn_mp4.configure(text=str(steam_mp4)[47:53].replace('"','') + " | " + str(steam_mp4.filesize_mb) +" MB")
    label_mp4.pack()
    btn_mp4.pack()



def mp3_dl():



#thumbnail_image
image_thumbnail = ctk.CTkImage(light_image=Image.open("assets/img/youtube_logo.jpg"), size=(width,height))
label_image = ctk.CTkLabel(window, text="")
#widget
url_label = ctk.CTkLabel(window, text='Enter URL')
url_entry = ctk.CTkEntry(window, width=width)
link = url_entry.get()

label_mp3 = ctk.CTkLabel(window, text='mp3')
label_mp4 = ctk.CTkLabel(window, text='mp4')
btn_mp3 = ctk.CTkButton(window, text='', command=mp3_dl)
btn_mp4 = ctk.CTkButton(window, text='')

#reso_box = ctk.CTkOptionMenu(window, values=option)

#Progress Bar
dl_progress = ctk.CTkProgressBar(window, width=width)
dl_progress.set(0)

#Button Download
dl_btn = ctk.CTkButton(window, text='Submit', command=clicker)

percen_label = ctk.CTkLabel(window, text=str(dl_progress.get()) + '%')
info_label = ctk.CTkLabel(window, text='')
duration_label = ctk.CTkLabel(window, text='')

#run
url_label.pack(pady=10)
url_entry.pack(pady=10)
dl_btn.pack(pady=10)
label_image.pack()
info_label.pack(pady=5)
duration_label.pack(pady=5)
# dl_progress.pack(pady=10)
# percen_label.pack()

window.mainloop()