from tkinter import *
import customtkinter as ctk
import tkinter.font as ctkfont 
from PIL import Image, ImageTk

ctk.set_appearance_mode('light')
#ctk.set_default_color_theme('blue')

top = ctk.CTk()
top.title("Feedback form")
top.geometry("1080x720")
top.resizable(False, False)

image_path = r"C:\python\my pydb projects\practice cust\software project\yt_qt raj\images\recaptcha.jpeg"
logo_image = Image.open(image_path)
logo_image = logo_image.resize((100, 60))
logo_ctk = ImageTk.PhotoImage(logo_image)

logo_label = ctk.CTkLabel(top, image=logo_ctk, text="")
logo_label.place(x=900, y=520)  

label_contact = ctk.CTkLabel(top, text = "Contact Us",text_color='Purple',font=("Helvetica",20))
label_contact.place(x=170, y=195)

label_title= ctk.CTkLabel(top, text = "Get in touch\ntoday", font=ctk.CTkFont(size=40, weight="bold"), justify="left")
label_title.place(x=170, y=230)

label_subtitle = ctk.CTkLabel(top,text = "We’d love to hear from you. Please fill out the form and we’ll get back to you soon!", justify="left",
    font=ctk.CTkFont(size=16),
    wraplength=400, 
    text_color="Green"
)
label_subtitle.place(x=170, y=330)

#email
label_email_info = ctk.CTkLabel(top,text ="📧 Email: vikrant@gmail.com",font=('Bold',20),text_color="#444444")
label_email_info.place(x=170, y=380)

#phone 
label_phone_info = ctk.CTkLabel(top,text ="📞 Phone: rollno 35",font=('Bold',20),text_color="#444444")
label_phone_info.place(x=170, y=430)

label_name = ctk.CTkLabel(top, text = "Full Name",font=("Helvetica",14))
label_name.place(x=700,y=160)

entry_name = ctk.CTkEntry(top, placeholder_text="Your Name", height=40, width = 280)
entry_name.place(x=700,y=190)

label_email = ctk.CTkLabel(top, text = "Email",font=("Helvetica",14))
label_email.place(x=700,y=230)

entry_email = ctk.CTkEntry(top, placeholder_text="Your Email Address", height=40, width = 280)
entry_email.place(x=700,y=260)

label_company = ctk.CTkLabel(top, text = "Company (Optional)",font=("Helvetica",14))
label_company.place(x=700,y=300)

entry_company = ctk.CTkEntry(top, placeholder_text="Company Name", height=40, width = 280)
entry_company.place(x=700,y=330)

label_msg = ctk.CTkLabel(top, text = "Leave us a message",font=("Helvetica",14))
label_msg.place(x=700,y=370)

entry_msg = ctk.CTkEntry(top, placeholder_text="Write your message here...", height=115, width = 280)
entry_msg.place(x=700,y=400)

keep_me_check = ctk.BooleanVar()
my_check= ctk.CTkCheckBox(top, text = "I'm not a robot",height = 0,width = 0,font=("Bold",18),
        variable=keep_me_check, onvalue='on', offvalue='off')
my_check.place(x=700,y=530)

button = ctk.CTkButton(top, text="Send Message", width=180, height=40)
button.place(x=700, y=600)

top.mainloop()
