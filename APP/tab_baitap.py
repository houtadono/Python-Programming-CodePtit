from tkinter import *
from tkinter.ttk import Style, Button, Combobox
from PIL import Image, ImageTk
from Code_ptit import *
from each_baitap import EachBaiTap
from tool_tip import ToolTip
from submit_dialog import SubmitDialog
class TabBaiTap(Frame): 
    def __init__(self, parent, code): 
        self.parent = parent
        self.code = code
        Frame.__init__(self,parent)
        self.id_ex = []
        self.my_bts = {}
        self.text_bts = {} 
        self.select_ids = []
        self.each_baitap = None
        self.init() 

    def init(self):
        self.style = Style()
        self.style.configure('TButton'     , foreground='#404040', font= ("SF Mono",10,"bold"))

        self.style.configure('Top.TButton' , foreground='#FF0000', font= ("SF Mono",10,"bold"), background='#FF0000')

        self.style.configure('Green.TButton'  , background='#19BE6B')
        self.style.configure('Red.TButton', background='#FF0000')
        self.style.configure('White.TButton', background='#FFFFFF')

        self.style.configure('Click.Green.TButton', foreground='#3333FF')
        self.style.configure('Click.Red.TButton', foreground='#3333FF')
        self.style.configure('Click.White.TButton', foreground='#3333FF')

        top_frame = Frame(self,relief=GROOVE)
        top_frame.pack(side=TOP,fill=BOTH,expand=True)
        
        self.textBtSelect = StringVar()
        self.textBtSelect.set("Chọn nhiều")
        selectBt = Button(top_frame, textvariable= self.textBtSelect, style='Top.TButton', command=self.select)
        selectBt.pack(side=LEFT,padx=0,pady=2)

        self.txt_select = StringVar()
        self.lbl_select = Label(top_frame, textvariable=self.txt_select)
        self.lbl_select.pack_forget()

        self.submitBt = Button(top_frame, text='Submit', command= self.open_submit_dialog)
        self.submitBt.pack_forget()

        option = [
            "hello",
            "cmnm",
            "zzza",
            "ttttk"
        ]

        imglbl = ImageTk.PhotoImage(Image.open('./APP/image/Rectangle 1.png'))
        
        lbl_search = Label(top_frame,image=imglbl)
        lbl_search.image = imglbl
        lbl_search.pack(side=RIGHT,padx=1,pady=2)

        self.searchEntry = Entry(lbl_search, width=19, border=0, font=("Segoe UI",11))
        self.searchEntry.place(x= 9, y= 6)
        self.searchEntry.bind("<Return>", lambda e: self.search())

        self.searchBt = Button(lbl_search, text='/', style='Top.TButton', width=2, command=self.search)
        self.searchBt.place(x= 170, y= 3)


        self.comboBox = Combobox(top_frame,values=option)
        self.comboBox.current(0)
        self.comboBox.bind("<<ComboboxSelect>>", self.comboClick)
        self.comboBox.pack(side=RIGHT)

        self.id_ex = self.code.ID
        self.load_ex()
        pass


    def comboClick(self):
        print(1)


    def open_submit_dialog(self):
        sub_dialog = SubmitDialog(self.parent, self, self.code, self.select_ids)
        self.select()


    def search(self):
        self.id_ex = self.code.find_exs_by_id_or_name(self.searchEntry.get().lower())
        print(self.id_ex)
        self.reload()

    def select(self):
        self.parent.update()
        if self.textBtSelect.get() == "Chọn nhiều":
            self.textBtSelect.set("Bỏ chọn")
            for id in self.id_ex:
                if self.my_bts[id].cget('style') == 'Green.TButton':
                    continue
                self.text_bts[id].set(f"{chr(10062)} {id}") # ❎
            self.lbl_select.pack(side=LEFT)
            self.submitBt.pack(side=LEFT)

        else:
            for id in self.select_ids:
                self.clickBtEx(id,False)
            self.select_ids = []
            self.textBtSelect.set("Chọn nhiều")
            for id in self.id_ex:
                self.text_bts[id].set(id)
            self.lbl_select.pack_forget()
            self.submitBt.pack_forget()

        self.update_text_select()

    def update_text_select(self):
        self.txt_select.set(f"Đã chọn: {len(self.select_ids)}")

    def clickBtEx(self, id,remove = True):
        if self.textBtSelect.get() == "Bỏ chọn":
            if self.text_bts[id].get() == f"{chr(9989)} {id}": # ✅
                # un select Ex
                if remove:
                    self.select_ids.remove(id)
                self.text_bts[id].set(f"{chr(10062)} {id}") # ❎
                old_style = self.my_bts[id].cget('style')
                self.my_bts[id].config(style= old_style.split('.',1)[1])
            elif self.text_bts[id].get() == f"{chr(10062)} {id}":
                # select Ex
                self.select_ids.append(id)
                self.text_bts[id].set(f"{chr(9989)} {id}") # ✅
                self.my_bts[id].config(style= 'Click.'+self.my_bts[id].cget('style'))
            self.update_text_select()
            # self.update()
        else:
            self.each_baitap = EachBaiTap(self.parent, self, self.code.EXERCISES[id], self.code)
            self.hide()
        pass
    
    def load_ex(self):
        padx = 5
        pady = 3

        cols = int(1000/(padx + 130))

        self.mid_frame = mid_frame = Frame(self)
        mid_frame.pack(fill=BOTH,expand=True)

        for i in range(len(self.id_ex)):
            ex = self.code.EXERCISES[self.id_ex[i]]
            self.text_bts[self.id_ex[i]] = StringVar()
            self.text_bts[self.id_ex[i]].set(f"{ex.id}")

            a = Button(mid_frame, textvariable= self.text_bts[self.id_ex[i]], command=lambda id = self.id_ex[i]: self.clickBtEx(id), 
                style=f"{ex.color}.TButton", width=13, cursor='hand2')
            a.grid(row=int(i/cols), column=i%cols, padx=padx, pady=pady)

            self.my_bts[self.id_ex[i]] = a

            ToolTip.create_tip(a, text=ex.info())      
        pass

    def reload(self):
        self.mid_frame.destroy()
        self.load_ex()

    def show(self):
        self.pack(fill=BOTH,expand=True)
    
    def hide(self):
        self.pack_forget()