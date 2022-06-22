import os
import webbrowser

#поиск pdf в указанной директории
def find(directory):
    res = []
    if directory:
        os.chdir(directory)

    for f in os.listdir():
        if f.endswith(".pdf"):
            res.append(os.path.join(f))

    return res

#открытие pdf
def open(name):
    webbrowser.open_new(name)



