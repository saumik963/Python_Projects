import tkinter
import customtkinter as ct
from pytube import YouTube
import os


# function area

def startDownload():
    progressbar.set(0)
    percent.configure('0%')


    try:
        ytlink = link.get()
        ytobj = YouTube(ytlink,on_progress_callback=on_progress)

        if res_op.get()=='mp3':
            video = ytobj.streams.filter(only_audio=True).first()
            filename = ytobj.title + '.mp3'

            filesize_mb = video.filesize / (1024 * 1024)


            title.configure(text=ytobj.title,text_color='green')
            file_size.configure(text=f'Size : {filesize_mb:.2f} MB' ,text_color='green')


            video.download(os.getcwd(),filename=filename)
            
        else:
            video = ytobj.streams.filter(res = res_op.get(), file_extension = "mp4").first()
            filesize_mb = video.filesize / (1024 * 1024)

            title.configure(text=ytobj.title,text_color='green')
            file_size.configure(text=f'Size : {filesize_mb:.2f} MB' ,text_color='green')

            video.download(os.getcwd())



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
app.geometry("400x250")
app.title("YT Downloader")


title= ct.CTkLabel(app,text="Insert YouTube Video Link")
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
finishLabel.place(x=140,y=210)

file_size= ct.CTkLabel(app,text="")
file_size.place(x=310,y=95)


app.resizable(False,False)
app.mainloop()