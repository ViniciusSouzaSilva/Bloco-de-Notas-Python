from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile

class MenuActions():
    def __init__(self):
        self.fileOpened = False

    def salvarArquivo(self):
        self.content = self.textA.get(1.0, END)

        if self.fileOpened == True:
            with open(self.file, 'w', encoding='utf-8') as txtFile:
                txtFile.write(self.content)
        else:
            self.salvarArquivoComo()

        print(self.content)

    def abrirArquivo(self):
        self.file = askopenfile(mode='r', filetypes=[('TXT Files', '*.txt')]).name
        self.fileOpened = True
        self.root.title(self.file)
        self.limparTextArea()

        with open(self.file, 'r', encoding='utf-8') as txtFile:
            for i in txtFile:
                self.textA.insert(END, i)

    def novoArquivo(self):
        print()

    def textAreaConfig(self):
        self.textA = Text(self.root)
        self.textA.place(rely=0, relx=0, relwidth=1, relheight=1)

    def salvarArquivoComo(self):
        self.file = asksaveasfile(initialfile='Untitled', defaultextension='.txt', filetypes=[('TXT Files', '*.txt')]).name
        with open(self.file, 'w', encoding='utf-8') as txtFile:
            txtFile.write(self.textA.get(1.0, END))
        self.fileOpened = True
        self.root.title(self.file)

    def limparTextArea(self):
        self.textA.delete(1.0, END)