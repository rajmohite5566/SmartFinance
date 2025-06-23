from tkinter import *
import customtkinter as ctk
import tkinter.font as ctkfont 

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('blue')

top = ctk.CTk()
top.title("Login Page")
top.geometry("600x400")

underline_font = ctk.CTkFont(family = "Helvetica", size=12,underline=True)  #to underline the forgot password 

left_side = ctk.CTkFrame(top,width=500,fg_color='#007bff')
left_side.pack(side = "left",fill="both",expand=True)

logo = ctk.CTkLabel(left_side, text = "Smart Finance",
                    font=ctk.CTkFont(size = 25,weight="bold"),
                    text_color = "white", justify="left")
logo.place(x=600,y=120)

descrp = ctk.CTkLabel(left_side, text="You are the one to use this..",
        font=ctk.CTkFont(size=25,weight='bold'),
        text_color='white')
descrp.place(x=500,y=180)

sign_in_box = ctk.CTkFrame(top, width=400, height=450, corner_radius=20, fg_color = "white", border_width=1, border_color="#cccccc",)
sign_in_box.place(relx = 0.72, rely = 0.5, anchor = "center")

label_1 = ctk.CTkLabel(top, text = "Sign in",font=("Helvetica",20),bg_color='white')
label_1.place(x=950,y=200)

label_2 = ctk.CTkLabel(top, text = "Don't have an account?Sign up",bg_color = "white")
label_2.place(x=950,y=228)

entry_email = ctk.CTkEntry(top, placeholder_text = "Email",width=250)
entry_email.place(x=950,y=260)

entry_password = ctk.CTkEntry(top, placeholder_text = "Password",show="*",width=250)
entry_password.place(x=950,y=310)

keep_me_check = ctk.BooleanVar()
my_check= ctk.CTkCheckBox(top, text = "Keep me Logged in",height = 0,width = 0,bg_color='white',
        variable=keep_me_check, onvalue='on', offvalue='off')
my_check.place(x=950,y=350)

submit_button = ctk.CTkButton(top,text = "Log in Now",height=35,width=250)
submit_button.place(x=950,y=390)

forgot_password = ctk.CTkLabel(top, text = "Forgot Password?",cursor="hand2", font=underline_font, text_color="blue",bg_color = "white")
forgot_password.place(x=1100,y=430)

social_media = ctk.CTkFrame(sign_in_box, fg_color = 'white')
social_media.place(x=950,y=450)

top.mainloop()
