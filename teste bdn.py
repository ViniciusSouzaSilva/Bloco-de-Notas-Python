import os
from tkinter.filedialog import askopenfile

p=[]

f = askopenfile(mode='r', filetypes=[('TXT files', '*.txt')]).name


with open(f,'r', encoding='utf-8') as txtteste:
    for i in txtteste:
        print(i.rstrip())

print(p)
