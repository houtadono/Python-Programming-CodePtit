from tkinter import *
from tkinter import filedialog
import os
from tkinter.ttk import Style

class SubmitDialog(Toplevel):
    def __init__(self, parent, tab_baitap, code, list_id):
        super(SubmitDialog,self).__init__(parent)
        parent.update()
        self.tab_bt = tab_baitap
        self.code = code
        self.list_id = list_id
        self.list_id_not_ac = list_id
        self.style = Style()
        self.style.theme_use("xpnative")

        self.geometry("414x150+573+119") # 418 422

        self.transient(parent)  # Make the self modal
        self.grab_set()  # Grab the focus for the self

        # Add widgets to the self
        top = Frame(self)
        top.pack(side=TOP)
        Label(top,text='Submit Code', font=('Segoe UI',17,'bold')).pack(side=TOP,pady=2)


        mid = Frame(self, borderwidth=2,relief="solid")
        mid.pack(side=TOP,fill='both')

        font_sub = ('Segie UI',14,'bold')
        self.creat_label_grid(mid,"Mã",font_sub,'blue').grid(row=0, column= 0,sticky="NSEW")
        self.creat_label_grid(mid,"Đường dẫn",font_sub,'blue').grid(row=0, column= 1,sticky="NSEW")
        self.creat_label_grid(mid,"  ",font_sub,'blue').grid(row=0, column= 2,sticky="NSEW")
        self.creat_label_grid(mid,"Trạng thái",font_sub,'blue').grid(row=0, column= 3,sticky="NSEW")

        self.entry_file = {}
        self.label_sub = {}
        max_width = 0
        for i in range(len(self.list_id)):
            id = self.list_id[i]
            
            e1 = self.creat_label_grid(mid,id,font_sub,'red')
            e1.grid(row=i+1, column= 0,sticky="NSEW")

            e2 = Entry(mid, width=20,borderwidth=1, relief='solid')
            e2.grid(row=i+1, column=1,sticky="NSEW")
            self.entry_file[id] = e2

            e3 = Button(mid,text="Chọn tệp",borderwidth=1,bg='white', relief='solid', command= lambda id = id: self.open_file_dialog(id) )
            e3.grid(row=i+1,column=2,sticky="NSEW") 

            e4 = frame_sub = Frame(mid, borderwidth=1,background='white', relief="solid")
            frame_sub.grid(row=i+1,column=3,sticky="NSEW")
            
            self.label_sub[id] = e = Label(frame_sub, text='        ',font=font_sub, bg='white')
            e.pack(side=LEFT)

            Button(frame_sub,text="Edit code",bg='white',borderwidth=0, command= lambda id = id: self.open_file_edit_code(id) ).pack(side=LEFT)
            Button(frame_sub,text="Nộp", bg='white',borderwidth=0, command= lambda id = id: self.click_bt_sub_grid(id) ).pack(side=LEFT)
            
            self.update()
            width_grids = e1.winfo_width()+e2.winfo_width()+e3.winfo_width()+e4.winfo_width()
            max_width = max(max_width,width_grids)

        bot = Frame(self)
        bot.pack(side=TOP,fill=X)
        Button(bot,text="Tự động chọn lấy đường dẫn tệp",padx=2,pady=10, command=self.click_bt_auto).pack(side= LEFT)
        Button(bot,text="Check empty file",padx=2,pady=10, command=self.click_bt_check).pack(side= LEFT)


        Button(self, text='Close', command=self.close).pack(side=LEFT)

        Button(self, text='Submit no AC',padx=20, command= lambda lst = self.list_id_not_ac:self.click_bt_sub_list(lst) ).pack(side=RIGHT)
        Button(self, text='Submit All',padx=20, command= lambda lst = self.list_id:self.click_bt_sub_list(lst) ).pack(side=RIGHT)

        self.geometry('{}x{}'.format(max_width+3, 150+31*len(self.list_id) ))
        pass

    @staticmethod
    def creat_label_grid(parent, text,font, fg ):
        return Label(parent, text=text,padx=10, font=font, fg=fg, bg='white', anchor='w',borderwidth=1, relief='solid')

    def open_file_dialog(self, id):
        file_path = filedialog.askopenfilename()
        self.update()
        print(self.winfo_width(),self.winfo_height(),self.winfo_x(),self.winfo_y())
        
        self.entry_file[id].delete(0,END)
        self.entry_file[id].insert(0,file_path)
        self.entry_file[id].xview('end')

    def open_file_edit_code(self, id):
        path = self.entry_file[id].get().strip()
        os.startfile(path)

    def click_bt_sub_grid(self, id):
        path = self.entry_file[id].get().strip()
        if path =='' or path == '# empty':
            return
        status = self.code.upload_code(id,self.entry_file[id].get().strip())
        if status == None:
            return
        res = self.code.get_result(id, status)
        self.label_sub[id].config(text=res[0],fg=res[1])
        if res[0] == 'AC':
            self.list_id_not_ac.remove(id)

    def click_bt_auto(self):
        for id in self.list_id:
            path = self.entry_file[id].get().strip()
            if path =='' or path == '# empty':
                self.entry_file[id].delete(0,END)
                path = "{}\\{}.py".format(self.code.EXERCISES[id].topic,id)
                self.entry_file[id].insert(0,os.path.abspath(path=path))
                self.entry_file[id].xview('end')

    def click_bt_check(self):
        for id in self.list_id:
            path = self.entry_file[id].get().strip()
            if path == '' or path == '# empty':
                continue
            check_empty = True
            with open(file=path) as f:
                for i in f.readlines()[::-1]:
                    if "# done" in i:
                        check_empty = False
                        break
                    if "# empty" in i:
                        break
            if check_empty:
                self.entry_file[id].delete(0,END)
                self.entry_file[id].insert(0,"# empty")

    def click_bt_sub_list(self, lst):
        status_res = {}
        
        for id in lst:
            path = self.entry_file[id].get().strip()
            if path == '' or path == '# empty':
                continue
            status = self.code.upload_code(id,path)
            status_res[id] = status

        for id in status_res.keys():
            if status_res[id] == None:
                return
            result = self.code.get_result(id,status_res[id])
            self.label_sub[id].config(text=result[0], fg=result[1])
            if result[0] == 'AC':
                self.list_id_not_ac.remove(id)

    def close(self):
        self.tab_bt.reload()
        self.destroy()
    