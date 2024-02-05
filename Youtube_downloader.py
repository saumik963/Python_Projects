import tkinter
import customtkinter as ct
from pytube import YouTube
import os,webbrowser
import ctypes



# function area

def startDownload():
    progressbar.set(0)
    percent.configure('0%')


    try:
        ytlink = link.get()
        ytobj = YouTube(ytlink,on_progress_callback=on_progress)
        path=path_loc.get()

        if res_op.get()=='mp3':
            video = ytobj.streams.get_audio_only()

            filesize_mb = video.filesize / (1024 * 1024)


            title.configure(text=ytobj.title,text_color='green')
            file_size.configure(text=f'Size : {filesize_mb:.2f} MB' ,text_color='green')


            
        else:
            video = ytobj.streams.filter(res = res_op.get(), file_extension = "mp4").first()
            filesize_mb = video.filesize / (1024 * 1024)

            title.configure(text=ytobj.title,text_color='green')
            file_size.configure(text=f'Size : {filesize_mb:.2f} MB' ,text_color='green')

        video.download(path)



        finishLabel.configure(text="Download Complete",text_color='green')
    except:
        finishLabel.configure(text="Download Incomplete!",text_color='red')
        
def on_progress(stream,chunk,bytes_remaining):
    total_size=stream.filesize
    bytes_downloaded=total_size-bytes_remaining
    percentage= bytes_downloaded / total_size * 100
    per= str(int(percentage))
    percent.configure(text=per +'%')
    percent.update()

    progressbar.set(float(percentage)/100)



options=["360p","720p","1080p","mp3"]


ct.set_appearance_mode("System")
ct.set_default_color_theme("blue")

app= ct.CTk()
app.geometry("400x290")
app.title("YT Downloader")

# taskbar logo
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

app.iconbitmap(r'C:\Users\Saumik\Desktop\Python\Python practices\YTD\youtube-logo.ico')


title= ct.CTkLabel(app,text="Insert YouTube Video Link",font=("Protest Strike",14))
title.pack(padx=10,pady=10)

url_var=tkinter.StringVar()
link=ct.CTkEntry(app,width=350,height=40,textvariable=url_var)
link.pack()

# resulation option 

res_op=ct.CTkOptionMenu(app,values=options)
res_op.place(x=25,y=100)
res_op.set("720p")





# porgress bar
percent=ct.CTkLabel(app,text="0%")
percent.pack(pady=10)

progressbar=ct.CTkProgressBar(app,width=300)
progressbar.set(0)
progressbar.place(x=50,y=150)

download= ct.CTkButton(app,text="Download" , command=startDownload)
download.place(x=130,y=170)

finishLabel= ct.CTkLabel(app,text="")
finishLabel.place(x=140,y=200)

file_size= ct.CTkLabel(app,text="")
file_size.place(x=310,y=95)

# path choose

pathLabel= ct.CTkLabel(app,text="Download to ")
pathLabel.place(x=25,y=232)

path_address=tkinter.StringVar(value=os.getcwd())
path_loc=ct.CTkEntry(app,width=280,height=30,textvariable=path_address)
path_loc.place(x=100,y=230)


# About

about= ct.CTkLabel(app,text="Created By SDA",text_color='green',cursor='hand2',font=('Orbitron',11,'bold'))
about.place(x=290,y=262)
about.bind('<Button-1>',lambda x:webbrowser.open_new("https://saumik963.pythonanywhere.com/"))

app.resizable(False,False)
app.mainloop()
