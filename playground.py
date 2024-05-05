import os.path
import os
import customtkinter as ctk

root = ctk.CTk()
root.geometry('480x480')

colors = ["Red", "Green", "Blue"]
option1 = ctk.CTkOptionMenu(root, values=colors)

print(os.getenv('HOME'))

option1.pack(pady=10)
root.mainloop()