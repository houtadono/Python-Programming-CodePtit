from tkinter import Tk, BOTH, TOP, NW, Entry, Button, Checkbutton, BooleanVar
from tkinter.ttk import Frame, Style, Label, Checkbutton
from PIL import Image, ImageTk
from configparser import ConfigParser
from Code_ptit import *
from loading import Loading

class Login(Frame): 
    def __init__(self, parent, code): 
        super(Login,self).__init__(parent)
        self.parent = parent
        self.code = code
        self.initUI() 


    def initUI(self): 
        self.parent.title("Đăng nhập")
        self.style = Style()
        self.style.theme_use("xpnative")
        self.pack(fill=BOTH, expand=1)
        
        imgLogo = ImageTk.PhotoImage(Image.open("./APP/image/logo_ptit.png"))
        imgNotice = ImageTk.PhotoImage(Image.open("./APP/image/notice.png"))
        imgEntry = ImageTk.PhotoImage(Image.open('./APP/image/Rectangle 1.png'))

        self.configs = ConfigParser()
        self.configs.read('./APP/login.properties')
        username = self.configs['form']['user']
        password = self.configs['form']['pass']
        remember = self.configs['form']['remember']

        # logo
        logo = Frame(self)
        logo.pack(side=TOP)

        lbl1 = Label(logo, image=imgLogo)
        lbl1.image = imgLogo
        lbl1.pack(side= TOP, pady= (10,0))
        Label(logo, text= "Đăng nhập", font=("Arial",  14)).pack(side=TOP, pady=1)
        Label(logo, text= "PTIT Code", font=("Arial",  13)).pack(side=TOP, pady=0)

        self.notice_f = Frame(logo)
        self.notice_f.pack(side=TOP, pady=0)

        self.notice_i = Label(self.notice_f, image=imgNotice)
        self.notice_i.image = imgNotice
        self.notice_i.pack_forget()

        self.notice = Label(self.notice_i, font=("Segeo UI", 9),foreground="red", background="white", border=0)
        self.notice.place(x= 30, y= 23)

        # form
        form = Frame(self, width= 270, height=100)
        form.pack(side= TOP, pady= 0)
        ## user
        Label(form, text="Tài khoản").pack(side=TOP, anchor=NW)
        lblEntry = Label(form, image=imgEntry, border=0)
        lblEntry.image = imgEntry
        lblEntry.pack(padx=0)
        self.userEntry = Entry(lblEntry, width= 31, border= 0)
        self.userEntry.insert(0,username)
        self.userEntry.place(x= 10, y= 7)
        ##pass
        Label(form, text="Mật khẩu").pack(side= TOP, anchor=NW, pady= (10,0))
        lblEntry = Label(form, image=imgEntry, border=0)
        lblEntry.image = imgEntry
        lblEntry.pack(padx=0)
        self.passEntry = Entry(lblEntry, show="\u2022", width= 31, border= 0)
        self.passEntry.insert(0,password)
        self.passEntry.place(x= 10, y= 7)

        self.remember = BooleanVar()
        if remember == '1': 
            self.remember.set(True)

        cb = Checkbutton(form, text= "Ghi nhớ", variable=self.remember, cursor="hand2")
        cb.pack(side=TOP, anchor=NW, pady=(5,2))

        imgBt = ImageTk.PhotoImage(Image.open('./APP/image/loginBt.png'))
        bt = Button(form, image=imgBt, text= "Đăng nhập", border=0, command=self.login, cursor="hand2")
        bt.image = imgBt
        bt.pack(fill= 'x', side= TOP,expand= True)

    def write_properties(self, username = '', password = '', remember = ''):
        self.configs['form']['user'] = username
        self.configs['form']['pass'] = password
        self.configs['form']['remember'] = remember
        with open('./APP/login.properties', 'w') as configfile:
            self.configs.write(configfile)


    def login(self):
        username, password = self.userEntry.get(),self.passEntry.get()
        check, notice = self.code.login(username, password)
        if not check:
            arr = notice.split(" ")
            for i in range(len(arr)):
                if i % 7 == 6:
                    arr[i] = "\n" + arr[i]
            notice = ' '.join(arr)

            self.notice_i.pack(side=TOP)
            self.notice.config(text= notice)
            if "\n" in notice:
                self.notice.place(x= 30, y= 23)
            else:
                self.notice.place(x= 30, y= 26)

            if self.parent.winfo_height() >= 430:
                return
            self.parent.geometry("%dx%d+%d+%d" %(self.parent.winfo_width(), 430 , self.parent.winfo_x(),self.parent.winfo_y()))
        else:
            Loading(self.parent,self.code)

        if check and self.remember.get():
            self.write_properties(username, password, '1')
        else:
            self.write_properties()
    

def display_msg():
    msg = Label(root, text='Thank You!')
    msg.pack()
    root.after(3000, root.quit)


if __name__ == "__main__":
    root = Tk()
    root.geometry("300x380+614+187")
    root.configure(background="white")
    # root.update()

    code = 1
    code = CodePtit()
    start = Login(root,code)
    root.protocol('WM_DELETE_WINDOW', display_msg)
    root.mainloop()
    code.driver.quit()