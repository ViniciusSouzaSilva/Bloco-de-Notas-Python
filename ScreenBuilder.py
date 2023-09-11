from tkinter import *
from MenuActions import MenuActions

class ScreenBuilder(MenuActions):
    def __init__(self):
        self.root = Tk()
        self.rootConfig()
        self.menuBarConfig()
        self.textAreaConfig()

        self.root.mainloop()
    def rootConfig(self):
        winWidth = int(self.root.winfo_screenwidth()/3)
        winHeight = int(self.root.winfo_screenheight()/1.4)
        scWidth = self.root.winfo_screenwidth()
        scHeight = self.root.winfo_screenheight()

        self.root.title('Bloco de Notas')

        self.root.geometry(f'{winWidth}x{winHeight}+{int(scWidth/2) - int(winWidth/2)}+{int(scHeight/2.3) - int(winHeight/2)}')

    def menuBarConfig(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        menuArquivo = Menu(menubar, tearoff=0)
        menuArquivo.configure(borderwidth=10)

        menubar.add_cascade(label='Arquivo', menu=menuArquivo)
        menuArquivo.add_command(label='Salvar', command=self.salvarArquivo)
        menuArquivo.add_command(label='Abrir', command=self.abrirArquivo)
        menuArquivo.add_command(label='Novo', command=self.novoArquivo())

