import customtkinter as ctk
from pytube import YouTube
from PIL import Image, ImageTk
import requests
import datetime

window = ctk.CTk()
window.geometry('720x480')
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
    info_label.configure(text=yt.title)
    duration_label.configure(text="Duration: " + str(datetime.timedelta(seconds=yt.length)))
    label_image.configure(image=image_thumbnail, width=width, height=height)
    image_thumbnail.configure(light_image=Image.open(requests.get(yt.thumbnail_url, stream=True).raw),size=(width,height))
    #steam = yt.streams.filter(res=reso_box, progressive=True).first()
    #steam = yt.streams.order_by().desc().first()
    #steam = yt.streams.get_by_resolution(reso_box.get())
    #steam.download(output_path='/Users/hara/Desktop/DL')

#thumbnail_image
image_thumbnail = ctk.CTkImage(light_image=Image.open("assets/img/youtube_logo.jpg"), size=(width,height))
label_image = ctk.CTkLabel(window, text="")
#widget
url_label = ctk.CTkLabel(window, text='Enter URL')
url_entry = ctk.CTkEntry(window, width=width)
link = url_entry.get()

#select_resolution
#option = ['360p','480p','720p']
tab_select = ctk.CTkTabview(window, width=200, height=250)
tab_mp3 = tab_select.add('Mp3')

btn_320 = ctk.CTkButton(tab_mp3,text="(.mp3) | 320kbps")
btn_256 = ctk.CTkButton(tab_mp3,text="(.mp3) | 256kbps")
btn_192 = ctk.CTkButton(tab_mp3,text="(.mp3) | 192kbps")
btn_128 = ctk.CTkButton(tab_mp3,text="(.mp3) | 128kbps")
btn_64 = ctk.CTkButton(tab_mp3,text="(.mp3) | 64kbps")
btn_320.pack()
btn_256.pack(pady=5)
btn_192.pack()
btn_128.pack(pady=5)
btn_64.pack()

tab_mp4 = tab_select.add('Mp4')

btn_360 = ctk.CTkButton(tab_mp4,text="(.mp4) | 1080p")
btn_720 = ctk.CTkButton(tab_mp4,text="(.mp4) | 720p")
btn_1080 = ctk.CTkButton(tab_mp4,text="(.mp4) | 360p")
btn_360.pack()
btn_720.pack(pady=5)
btn_1080.pack()

#reso_box = ctk.CTkOptionMenu(window, values=option)

#Progress Bar
dl_progress = ctk.CTkProgressBar(window, width=width)
dl_progress.set(0)

#Button Download
dl_btn = ctk.CTkButton(window, text='DOWNLOAD', command=clicker)

percen_label = ctk.CTkLabel(window, text=str(dl_progress.get()) + '%')
info_label = ctk.CTkLabel(window, text='Title')
duration_label = ctk.CTkLabel(window, text='Duration')

#run
url_label.pack(pady=10)
url_entry.pack(pady=10)
label_image.pack()
tab_select.pack()
info_label.pack(pady=5)
duration_label.pack(pady=5)
#reso_box.pack(pady=10)
dl_btn.pack(pady=10)
dl_progress.pack(pady=10)
percen_label.pack()

window.mainloop()