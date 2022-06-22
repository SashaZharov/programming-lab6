from tkinter import *
from fpdf import FPDF
from datapy import main as send_to_sheet
import datetime

copy_data = []
button_data = []

def build():
    res = []
    for i in range(len(button_data)):
        if i != len(button_data) - 1:
            res.append(button_data[i].get())
    send_to_sheet(res)
    create_file(copy_data, res, button_data[-1].get())

#верстка основного экрана
def main_screen(data):
    global copy_data
    copy_data = data
    window = Tk()
    window.geometry("800x600")
    window.title("Задание 2")

    for i in data:
        string = Frame(window)
        string.pack()

        label = Label(string, text=i, padx=5, pady=5)
        label.pack(side=LEFT)

        entry = Entry(string, width=15)
        entry.pack(side=LEFT)
        button_data.append(entry)

    string_file_name = Frame(window)
    string_file_name.pack()

    label = Label(string_file_name, text="Название pdf", padx=5, pady=5)
    label.pack(side=LEFT)

    entry = Entry(string_file_name, width=15)
    entry.pack(side=LEFT)
    button_data.append(entry)

    string_last = Frame(window)
    string_last.pack()
    Button(string_last, text="Посчитать", command=build, padx=5, pady=5).pack(side=LEFT)

    window.mainloop()

#создание таблицы с pdf
def create_file(data, res, name):
    table = []
    for i in range(len(data)):
        table.append([str(data[i]), str(res[i])])
 
    pdf = FPDF()
    pdf.set_font("Arial", size=12)
    pdf.add_page()
 
    col_width = pdf.w / 4.5
    row_height = pdf.font_size
    for row in table:
        for item in row:
            pdf.cell(col_width, row_height,
                     txt=item, border=1)
        pdf.ln(row_height)
 
    pdf.output(str(datetime.datetime.now()).split()[0] + " " + name + ".pdf")

