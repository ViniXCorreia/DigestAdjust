from tkinter import *
from pathlib import Path
from tkinter import messagebox
import os

class Window:
    def __init__(self, Master = None):
        self.frame = Frame(Master)
        self.frame.pack()
        self.imagec4 = Label(self.frame, image = img)
        self.imagec4.grid(row=0, columnspan= 4, sticky = N)
        self.textInput = Label(self.frame)
        self.textInput["text"] = "Entre com a chave de acesso:"
        self.textInput["font"] = "Calibri, 12"
        self.textInput["anchor"] = E
        self.textInput.grid(row = 1, column=0, padx =20, pady=20, sticky=E)
        self.input = Entry(self.frame)
        self.input["font"] = "Calibri, 12"
        self.input["width"] = 45
        self.input["bd"] = 2
        self.input.grid(row=1, column=1, columnspan=3, padx=5, sticky=E)
        self.ok = Button(self.frame)
        self.ok["text"] = "Ajustar"
        self.ok["font"] = "Calibri, 12"
        self.ok["width"] = 10
        self.ok["command"] = self.checkEntry
        self.ok.grid(row=2, column=3, padx=5, pady = 5, sticky=W)
        self.end = Button(self.frame)
        self.end["text"] = "Finalizar"
        self.end["font"] = "Calibri, 12"
        self.end["width"] = 10
        self.end["command"] = self.closeWindow
        self.end.grid(row=2, column=3, padx=0, pady = 5, sticky=E)

    def checkEntry(self):
        keyXML = self.input.get()
        if keyXML.isnumeric() and len(keyXML) == 44:
            self.deleteXML(keyXML)
        elif keyXML.isnumeric() and len(keyXML) < 44:
            messagebox.showerror("Ajusta Digest Value", "Esta faltando números na chave de acesso!")
        elif keyXML.isnumeric() and len(keyXML) > 44:
            messagebox.showerror("Ajusta Digest Value", "Entre apenas com os 44 os números da chave de acesso!")
        else:
            messagebox.showerror("Ajusta Digest Value", "Entre apenas com números!")

    def deleteXML(self, keyXML):
        nfeXML = "-nfe.xml"
        for root, dirs, files in os.walk(dirUsed):
            for dir in dirs:
                if dir.lower() == "lognfce":
                    keyXML += nfeXML
                    pathLogNfe = os.path.join(root,dir)
                    pathKeyXml = os.path.join(pathLogNfe, keyXML)
                    os.remove(pathKeyXml)
                    messagebox.showwarning("Ajusta Digest Value", "Abra o seu Emissor de NFCe e consulte a nota novamente!")
    
    def closeWindow(self):
        root.quit()


root = Tk()
root.title("Ajusta Digest Value")
width_window = 700
height_window = 430
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
posx = screen_width/2 - width_window/2
posy = screen_height/2 - height_window/2
root.geometry("%dx%d+%d+%d" %(width_window, height_window, posx, posy))
root.resizable(width=False, height=False)
dirUsed = os.getcwd()
root.iconbitmap(os.path.join(dirUsed, "Imagens\c4red.ico"))
img = PhotoImage(file= os.path.join(dirUsed, "Imagens\c4.png"))
Window(root)
root.mainloop()

