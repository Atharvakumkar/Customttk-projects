from tkinter import *
import customtkinter as ctk

ctk.set_appearance_mode("dark")

root = ctk.CTk()

root.title("Atharva Kumkar")
root.geometry("600x350")

def submit():
    label.configure(text=f"Hello {entry.get()} good to see you!")

label = ctk.CTkLabel(root, 
                     text="",
                     font=("Helvetica", 20))
label.pack(pady=40)

entry = ctk.CTkEntry(root,
                     placeholder_text="Enter your name")
entry.pack(pady=20)

button = ctk.CTkButton(root,
                       text="Submit",
                       text_color = "black",
                       fg_color = "white",
                       hover_color = "yellow",
                       height=70,
                       width=100,
                       command=submit)
button.pack(pady=50)

root.mainloop()
