import customtkinter as ctk

root = ctk.CTk()

colors = ["Red", "Green", "Blue"]
option1 = ctk.CTkOptionMenu(root, values=colors)


#run
option1.pack(pady=10)
root.mainloop()