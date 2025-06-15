from tkinter import *
import customtkinter as ctk

ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.title("Atharva Kumkar")
root.geometry("600x350")

label1 = ctk.CTkLabel(root, text="  Please read the instructions given below!  ",
                      text_color="white",
                      fg_color="grey")
label1.pack(pady=10)

inst = ctk.CTkScrollableFrame(root, 
                              height=200, 
                              width=500)
inst.pack(pady=10)

radio_value = ctk.StringVar(value="none")

label2 = ctk.CTkLabel(inst, 
                      text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer sit amet turpis efficitur magna suscipit consequat et vitae mauris. Vivamus tempus iaculis sem, ac pharetra urna convallis ut. Curabitur diam ex, posuere eu nisl eu, accumsan vulputate enim. Suspendisse aliquet ultricies sem ac fermentum. Interdum et malesuada fames ac ante ipsum primis in faucibus. Quisque volutpat orci ut dui auctor, et sollicitudin tortor tempor. Duis hendrerit ex sed lectus pellentesque placerat. Suspendisse nisl tortor, pretium ut vestibulum id, interdum quis neque. Fusce congue libero vel ipsum convallis, gravida luctus risus scelerisque. Sed et tellus ut nibh posuere semper id at tellus.',
                      wraplength=480)
rad_button = ctk.CTkRadioButton(inst, 
                                text = "I have read the information",
                                value = "Yes", 
                                variable = radio_value)
sub_button = ctk.CTkButton(root, 
                           text = "Submit")

label2.pack(padx=10, pady=10)
rad_button.pack(padx=10, pady=10)
sub_button.pack(padx=10,pady=10)

root.mainloop()
