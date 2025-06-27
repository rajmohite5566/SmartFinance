from tkinter import *
import customtkinter as ctk
import tkinter.font as ctkfont 

ctk.set_appearance_mode("dark")

top = ctk.CTk()
top.title("Login Page")
top.geometry("1080x720")
top.resizable("false", "false")

my_font_heading = ctk.CTkFont(family="Gotham-Bold", size = 42)
my_font_subheading = ctk.CTkFont(family="Gotham-Bold", size = 30)
my_font_label1 = ctk.CTkFont(family="Gotham-Bold", size = 30)
my_font_label2 = ctk.CTkFont(family="Gotham-Bold", size = 20)
my_font_button = ctk.CTkFont(family="Gotham-Bold", size = 20, underline = True)


top_main_frame = ctk.CTkFrame(master=top, width=1080, height=720, fg_color="#D3ECCD")
top_main_frame.place(x=0, y=0)

logo = ctk.CTkLabel(top_main_frame, 
                    text = "BudgetBee",
                    font= my_font_heading,
                    text_color = "#06923E",
                    justify="left")
logo.place(x=40,y=280)

descrp = ctk.CTkLabel(top_main_frame, 
                      text="Smart finance for smarter students",
                      font = my_font_subheading,
                      text_color = "#06923E")
descrp.place(x=40,y=340)

sign_in_box = ctk.CTkFrame(top, 
                           width=400, 
                           height=400, 
                           corner_radius=20, 
                           fg_color = "white",
                           bg_color = "white", 
                           border_color="#cccccc",)
sign_in_box.place(x = 600, y = 150)

label_1 = ctk.CTkLabel(master = sign_in_box, 
                       text = "Sign in",
                       font=my_font_label1,
                       text_color = "#06923E")
label_1.place(x = 20,y = 20)

label_2 = ctk.CTkLabel(master = sign_in_box, 
                       text = "Don't have an account? ",
                       font = my_font_label2,
                       text_color = "#06923E")
label_2.place(x = 20, y = 65)

signup_button = ctk.CTkButton(master = sign_in_box,
                             text = "Sign Up",
                             font = my_font_button,
                             height = 30,
                             width = 50,
                             text_color = "#06923E",
                             fg_color = "white",
                             hover_color = "white",
                             command = "")
signup_button.place(x = 262,y = 64)

line = ctk.CTkFrame(master = sign_in_box, 
                           width=350, 
                           height=2, 
                           bg_color = "#06923E")
line.place(x = 20, y = 120)

entry_email = ctk.CTkEntry(master = sign_in_box,
                           font = my_font_label2,
                           placeholder_text = "Email",
                           width = 350,
                           height = 40,
                           fg_color = "white",
                           border_color = "#06923E")
entry_email.place(x = 20, y = 150)

password_email = ctk.CTkEntry(master = sign_in_box,
                           font = my_font_label2,
                           placeholder_text = "Password",
                           width = 350,
                           height = 40,
                           fg_color = "white",
                           border_color = "#06923E")
password_email.place(x = 20, y = 205)

login_button = ctk.CTkButton(master = sign_in_box,
                             text = "Login Now",
                             font = my_font_button,
                             height = 40,
                             width = 350,
                             text_color = "#D3ECCD",
                             fg_color = "#06923E",
                             hover_color = "#045B27",
                             command = "")
login_button.place(x = 20,y = 275)


top.mainloop()
