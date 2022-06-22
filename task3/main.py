from tkinter import *
from functions import find
from functions import open
directory = None
window = None

#задаем каждой кнопке имя файла
class Button_Class:
    def __init__(self, string, name):
        self.name = name
        self.button = Button(string, text="Открыть", command= self.open_file, padx=5, pady=5).pack(side=LEFT)

    def open_file(self):
        open(self.name)

def build():
    name = directory.get()
    window.destroy()
    main(find(name))

def main(array):
    global directory
    global window 
    window = Tk()
    window.geometry("800x600")
    window.title("Найти pdf")

    str1 = Frame(window)
    str2 = Frame(window)

    str1.pack()
    str2.pack()

    Label(str1, text="Введите другую дирректорию ", padx=5, pady=5).pack(side=LEFT)

    for i in array:
        string = Frame(window)
        string.pack()
        Label(string, text=i, padx=5, pady=5).pack(side=LEFT)
        Button_Class(string, i)

    directory = Entry(str1, width=15)
    directory.pack(side=LEFT)

    Button(str2, text="Изменить", command=build, padx=5, pady=5).pack(side=LEFT)

    window.mainloop()

main([])

