from tkinter import *
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")  # Can be "System", "Light", or "Dark"

root = ctk.CTk()
root.title("SmartFinance")
root.geometry("1080x720")
root.resizable(False, False)

main_frame = ctk.CTkFrame(master=root, width=1080, height=720, fg_color="#D3ECCD")
main_frame.place(x=0, y=0)

my_font = ctk.CTkFont(family="Gotham-Bold", size = 28)
my_font_button = ctk.CTkFont(family="Gotham-Bold", size = 18)

def about():
    print("About us")

company_name = ctk.CTkLabel(master=main_frame,
                            text="BudgetBee",
                            font= my_font,
                            text_color = "#06923E")
company_name.place(x=20, y=12)

about_button = ctk.CTkButton(master=main_frame,
                             text = "About",
                             font = my_font_button,
                             height = 30,
                             width = 50,
                             text_color = "#06923E",
                             fg_color = "#D3ECCD",
                             hover_color = "#D3ECCD",
                             command = about)
about_button.place(x = 710,y = 18)

services_button = ctk.CTkButton(master=main_frame,
                             text = "Services",
                             font = my_font_button,
                             height = 30,
                             width = 50,
                             text_color = "#06923E",
                             fg_color = "#D3ECCD",
                             hover_color = "#D3ECCD",
                             command = about)
services_button.place(x = 800,y = 18)

contact_button = ctk.CTkButton(master=main_frame,
                             text = "Contact",
                             font = my_font_button,
                             height = 30,
                             width = 50,
                             text_color = "#06923E",
                             fg_color = "#D3ECCD",
                             hover_color = "#D3ECCD",
                             command = about)
contact_button.place(x = 900,y = 18)

login_button = ctk.CTkButton(master=main_frame,
                             text = "Login",
                             font = my_font_button,
                             height = 30,
                             width = 50,
                             text_color = "#06923E",
                             fg_color = "#D3ECCD",
                             hover_color = "#D3ECCD",
                             command = about)
login_button.place(x = 1000,y = 18)

line = ctk.CTkFrame(master=main_frame, 
                           width=1080, 
                           height=2, 
                           bg_color = "#06923E")
line.place(x = 0, y = 65)

root.mainloop()
