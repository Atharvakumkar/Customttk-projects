from tkinter import *
import customtkinter as ctk

ctk.set_appearance_mode("dark")

root = ctk.CTk()

root.title("Atharva Kumkar")
root.geometry("600x350")

def get_rad():
    if radio_var.get() == "none":
        label1.configure(text="Maybe select a gender?")
    elif radio_var.get() == "F":
        label1.configure(text="Welcome aboard Lady!")
    else:
        label1.configure(text="Welcome aboard Gentleman!")
    

label2 = ctk.CTkLabel(root, text="What's your gender?")
label2.pack(pady=40)

radio_var = ctk.StringVar(value="none")

radio1 = ctk.CTkRadioButton(root, text = "Male", 
                            value="M", 
                            variable=radio_var,
                            hover_color = "red" )
radio1.pack(pady=10)

radio2 = ctk.CTkRadioButton(root, text = "Female", variable=radio_var, value="F")
radio2.pack(pady=10)

button1 = ctk.CTkButton(root, text = "Submit", command = get_rad)
button1.pack(pady=10)

label1 = ctk.CTkLabel(root,text="")
label1.pack(pady=10)

root.mainloop()



