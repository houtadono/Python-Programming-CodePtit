from tkinter import Frame, Tk

class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side=TOP,fill=BOTH,expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

    def show_frame(self, frame):
        


if __name__ == "__main__":
    root = Tk()

    root.geometry("300x380+614+187")
    root.configure(background="white")
    code = CodePtit()

    start = Login(root,code)

    root.protocol('WM_DELETE_WINDOW', display_msg)
    root.mainloop()
    code.driver.quit() 