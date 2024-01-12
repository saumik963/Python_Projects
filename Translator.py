from googletrans import LANGUAGES, Translator
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# functions

def trans():
    s_text = src_text.get(1.0, tk.END)
    src_l = ls.get()
    dst_l = ld.get()
    lan_src.configure(text=src_l.upper())
    lan_dst.configure(text=dst_l.upper())

    tra = Translator()
    result = None

    try:
        result = tra.translate(s_text, src=src_l, dest=dst_l)
        error_msg.configure(text="")

    except:
        error_msg.configure(text="An error occurs. Check your connection and try again!")

    # Update the destination text widget
    dst.delete(1.0, tk.END)

    if result is not None:
        dst.insert(tk.END, result.text)
    else:
        dst.insert(tk.END, "Translation failed")



# GUI design

root = ttk.Window(themename="darkly")

root.geometry("400x400")
root.title("Translator")
root.iconbitmap("C:/Users/Kaushik/Desktop/Python/Python practices/icon.ico")


lan=list(LANGUAGES.values())

head= ttk.Label(text="GUI Translator",font=('Poppins',28) ,bootstyle="inverse-dark")
head.pack(pady=20)

# source choose

ls=ttk.Combobox(values=lan,bootstyle="primary")
ls.place(x=225,y=80)
ls.set("english")

# source input

lan_src= ttk.Label(text="Select",font=('Poppins',15) ,bootstyle="inverse-dark")
lan_src.place(x=25,y=80)

src_text= ttk.Text(root,font=('Poppins',12),wrap="word")
src_text.place(x=25,y=120,height=80,width=350)



# Destination choose

ld=ttk.Combobox(values=lan,bootstyle="primary")
ld.place(x=225,y=250)
ld.set("bengali")


# Destination input

lan_dst= ttk.Label(text="Select",font=('Poppins',15) ,bootstyle="inverse-dark")
lan_dst.place(x=25,y=250)

dst= ttk.Text(root,font=('Poppins',12),wrap="word")
dst.place(x=25,y=290,height=80,width=350)

# button

b = ttk.Button(root, text="Translate", bootstyle="info-outline",command=trans)
b.place(x=165,y=210)


error_msg= ttk.Label(text="",font=('Poppins',10) ,bootstyle="danger")
error_msg.place(x=25,y=375)

root.resizable(False, False)

root.mainloop()


