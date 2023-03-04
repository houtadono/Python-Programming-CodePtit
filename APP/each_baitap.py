from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from configparser import ConfigParser
from Code_ptit import *
from tab_bangxephang import TabBangXepHang
from tool_tip import ToolTip

class EachBaiTap(Frame): 

    def __init__(self, parent, tab_bt, ex, code): 
        self.parent = parent # main frame app
        self.tab_bt = tab_bt
        self.ex = ex
        self.code = code
        self.tab_bt.covered = True
        Frame.__init__(self,self.parent)
        self.init() 
    
    def init(self):
        self.pack(fill=BOTH, expand=True)
        self.update()
        
        top_f = Frame(self)
        top_f.pack(side=TOP,fill=X,expand=True)
        btBack = Button(top_f,text="Trở về",command= self.back)
        btBack.pack(side=LEFT)
        Label(top_f,text=f"{self.ex.id} - {self.ex.name}", font=("Segoe UI",14,"bold"), foreground="red", border=0).pack(side=RIGHT)
        s = Style()
        

        tabs = Notebook(self)
        tabs.pack(side=TOP, fill=BOTH, expand=TRUE)

        frame1 = Frame(tabs, width=130)
        frame2 = Frame(tabs, width=130)

        tabs.add(frame1, text="Đề Bài")
        tabs.add(frame2, text="Tab Two")

        self.init_frame1(frame1)

    def init_frame1(self, frame1):
        s = Style()
        s.configure('Normal.TLabel', font=("Times New Roman", 12))
        attrs = self.code.see_ex(self.ex.id)
        a = attrs.p
        while a != None:
            if a.name == None or a.name == 'table':
                a = a.next_sibling
                continue
            if a.name == 'p':
                padx = 0
                pady = 2
            elif a.name == 'ul':
                padx = 5
                pady = 2
            a.find('span')
            for x in a:
                if hasattr(x,'text'):
                    if not x.text.isspace():
                        Label(frame1, text= f"{x.text}", style='Normal.TLabel').pack(side=TOP, anchor=NW, padx=padx, pady=pady)
                        # print(f"111{x.text}111")
            a = a.next_sibling
    
    def back(self):
        self.tab_bt.show()
        self.tab_bt.each_baitap = None
        self.destroy()
