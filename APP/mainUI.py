from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from configparser import ConfigParser
from Code_ptit import *
from tab_bangxephang import TabBangXepHang
from tab_baitap import TabBaiTap

class MainUI(Frame): 

    def __init__(self, parent, code): 
        parent.destroy()
        self.parent = Tk()
        self.code = code
        super(MainUI,self).__init__(self.parent)
        self.init() 

    def init(self):
        self.parent.title("Code ptit")
        self.style = Style()
        self.parent.geometry("1000x574+274+106")
        self.parent.overrideredirect(False)
        
        self.style.theme_use("xpnative")
        # self.style.theme_use("winnative")
        # self.style.theme_use("clam")
        
        self.style.configure('TFrame', borderwidth = 3)

        self.pack(fill=BOTH, expand=True)
        
        top_frame = PanedWindow(self, style='TFrame')
        top_frame.pack(side=TOP,fill=X)

        self.canvas = canvas = Canvas(self)
        canvas.pack(side=LEFT, fill=BOTH, expand=True, padx=1,pady=1)

        scrollbar = Scrollbar(self, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        canvas.configure(yscrollcommand=scrollbar.set, scrollregion=canvas.bbox("all"))
        canvas.bind('<Enter>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind('<MouseWheel>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        self.main_frame = Frame(canvas)
        canvas.create_window((0,0), window=self.main_frame, anchor=NW)

        self.tab_bt = TabBaiTap(parent=self.main_frame, code=self.code)

        self.tab_bxh = TabBangXepHang(parent=self.main_frame,code=self.code)

        self.style = Style()
        self.style.configure('TopMainUI.TButton' , foreground='#FF0000', font= ("SF Mono",10,"bold"), background='#FFFFFF')

        img_1 = PhotoImage(file="./APP/image/notebook.png")
        self.bt1 = bt1 = Button(top_frame,text="Bài tập", image=img_1,compound="left",
                        style='TopMainUI.TButton', command=lambda: self.click_bt1())
        bt1.image = img_1
        bt1.pack(side=LEFT,fill=Y,padx=0,pady=0)

        img_2 = PhotoImage(file="./APP/image/rank.png")
        self.bt2 = bt2 = Button(top_frame,text="Bảng xếp hạng", image=img_2,compound="left",
                        style='TopMainUI.TButton', command=lambda: self.click_bt2())
        bt2.image = img_2
        bt2.pack(side=LEFT,fill=Y,padx=0,pady=0)


    def click_bt1(self):
        self.hide_all_bt()
        self.tab_bt.show()
        self.parent.update()
        w = self.parent.winfo_width()
        if w == 1000:
            w = 1001
        else:
            w = 1000
        self.parent.geometry(f"{w}x574+274+106")
        pass

    def click_bt2(self):
        self.hide_all_bt()
        self.tab_bxh.show()

        pass

    def hide_all_bt(self):
        if self.tab_bt.each_baitap != None:
            self.tab_bt.each_baitap.destroy()
            self.tab_bt.each_baitap = None
        self.tab_bt.hide()
        self.tab_bxh.hide()
    

# root = Tk()
# a = MainUI(root,1)
# root.mainloop()

