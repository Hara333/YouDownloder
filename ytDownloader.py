import customtkinter as ctk
from pytube import YouTube

window = ctk.CTk()
window.geometry('720x480')
window.title('YouTube Downloader')

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
    steam = yt.streams.filter(res=reso_box, progressive=True).first()
    #steam = yt.streams.order_by().desc().first()
    #steam = yt.streams.get_by_resolution(reso_box.get())
    steam.download(output_path='/Users/hara/Desktop/DL')
    info_label.configure(text=yt.title)
    views_label.configure(text=yt.views)
    print(yt.)

#widget
url_label = ctk.CTkLabel(window, text='Enter URL')
url_entry = ctk.CTkEntry(window, width=300)

#select_resolution
option = ['360p','480p','720p']
reso_box = ctk.CTkOptionMenu(window, values=option)

#Progress Bar
dl_progress = ctk.CTkProgressBar(window, width=300)
dl_progress.set(0)

#Button Download
dl_btn = ctk.CTkButton(window, text='DOWNLOAD', command=clicker)

percen_label = ctk.CTkLabel(window, text=str(dl_progress.get()) + '%')
info_label = ctk.CTkLabel(window, text='Title')
views_label = ctk.CTkLabel(window, text='Views')

#run
url_label.pack(pady=10)
url_entry.pack(pady=10)
reso_box.pack(pady=10)
dl_btn.pack(pady=10)
dl_progress.pack(pady=10)
percen_label.pack()
info_label.pack(pady=10)
views_label.pack(pady=10)
window.mainloop()