from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from configparser import ConfigParser
from Code_ptit import *
from tool_tip import ToolTip

class TabBangXepHang(Frame): 
    def __init__(self, parent, code): 
        self.parent = parent
        self.code = code
        super(TabBangXepHang,self).__init__(parent)
        # Frame.__init__(self,parent)
        self.init() 
    
    def init(self):
        top_frame_ex = Frame(self,width=1000, height= 10, border=2)
        top_frame_ex.pack(side=TOP)
        Label(top_frame_ex,text="hello2").pack()
        pass

    def show(self):
        self.pack(fill=BOTH,expand=True)
    
    def hide(self):
        self.pack_forget()