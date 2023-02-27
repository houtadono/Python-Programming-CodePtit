from io import BytesIO
import time
from tkinter import Tk, BOTH, TOP, Frame, PhotoImage
from tkinter.ttk import  Style, Label, Progressbar
from PIL import Image
from threading import Thread
from Code_ptit import *
from app import App

class Loading(Frame): 
    def __init__(self, parent, code): 
        # parent.destroy()
        self.parent = parent
        self.code = code
        Frame.__init__(self,self.parent)
        self.init() 
        self.load()
        App(self.parent,code)

    def image_to_data(im):
        with BytesIO() as output:
            im.save(output, format="PNG")
            data = output.getvalue()
        return data

    def init(self):
        self.parent.title("Loading")
        self.style = Style()
        self.parent.geometry("360x360+605+246")
        self.parent.overrideredirect(True)
        
        self.style.theme_use("default")
        self.style.configure("red.Horizontal.TProgressbar", foreground='yellow', background='#FF441E',thickness=12, boder=4)

        self.pack(side=TOP,fill=BOTH, expand=1)

        file="./script/image/loading_data.gif"
        self.imgGif = Image.open(file)
        self.frames = self.imgGif.n_frames
        self.list_fr = []
        self.lbl = Label(self,text="ok")
        self.lbl.pack()

        self.bar = Progressbar(self.lbl, style="red.Horizontal.TProgressbar",orient="horizontal", 
            length=200, mode="determinate", value=0, maximum= 101)
        self.bar.place(x= 80, y= 310)

        self.lbl_load = Label(self.lbl,text=self.update_progress_label(), font=("Seogeo UI",12), background='#0061ff', foreground='white')
        self.lbl_load.place(x= 150, y = 155)
        
        self.lbl.bind("<Button-1>", self.animation(1))
        self.time = time.time()

        
    def update_progress_label(self):
        return f"{ round(self.bar['value']*100/101,2) }%"

    def load(self):
        loading = Thread(target= self.code.create_thread)
        loading.start()

        while True:
            if not loading.is_alive():
                self.bar['value'] = 101
                self.lbl_load.config(text= self.update_progress_label())
                self.parent.update()
                return
            else:
                if self.bar['value'] == 100:
                    continue
                if round(time.time()-self.time,1) == 1.2:
                    self.time = time.time()
                    self.bar['value'] += 5
                self.lbl_load.config(text= self.update_progress_label())
                self.parent.update()

    def animation(self,count):
        self.imgGif.seek(count)
        img = PhotoImage(data=Loading.image_to_data(self.imgGif)) # ignore
        self.list_fr.append(img)
        self.lbl.configure(image= img)
        self.lbl.image = img
        count += 1
        if count == self.frames:
            count = 1
        if self.bar['value'] != 101:
            self.parent.after(50,lambda :self.animation(count))
        
