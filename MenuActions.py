from tkinter import *
from tkinter.filedialog import askopenfile

class MenuActions():
    def __init__(self):
        print()

    def salvarArquivo(self):
        print()

    def abrirArquivo(self):
        content = []
        file = askopenfile(mode='r', filetypes=[('TXT Files', '*.txt')]).name

        with open(file, 'r', encoding='utf-8') as txtFile:
            for i in txtFile:
                content.append(i)
                self.textA.insert(END, i)

    def novoArquivo(self):
        print()

    def textAreaConfig(self):
        self.textA = Text(self.root)
        self.textA.place(rely=0, relx=0, relwidth=1, relheight=1)