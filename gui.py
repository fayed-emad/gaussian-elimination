from tkinter import *
from tkinter import ttk
from gaussian_methods import GaussianElimination, GaussJordanElimination
from utilities import casting_float
import os
import re


screen = Tk()
screen.geometry('600x650')
screen.title('task')

# create a main frame
main_frame = Frame(screen)
main_frame.pack(fill=BOTH, expand=1)

# create a canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# add a scrollbar to the canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure the Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# create another frame inside the canvas
second_frame = Frame(my_canvas)

# Add that new frame to a window in the canvas
my_canvas.create_window((0, 0), window=second_frame, anchor='nw')

heading = Label(second_frame, text="Gaussain elemination and Gaussian jordan elemination: ", font=("cairo", 17))
heading.pack()

numUnknown = Label(text='Enter numbers of rows', font=('cairo', 16))
numUnknown.place(x=20, y=50)
n = StringVar()

numUnknownEntry = Entry(textvariable=n, width=5, font=('Verdana', 14))
numUnknownEntry.place(x=280, y=55)


def restart():
    screen.destroy()
    os.system('python "C:\\Users\\bdbd\PycharmProjects\pythonProject1\\venv\linear_system_solver\gui.py"')


btn_start = Button(text='Restart Program', command=restart, font=('cairo', 16))
btn_start.pack(side=LEFT)

def destroy_and_return():
    global listRow
    global listLabel
    global gaussianBtn
    global jordanBtn
    global mat
    mat = []
    for i in range(len(listRow)):
        row = listRow[i].get()
        row = re.split('[\s]+', row.strip())
        mat.append(row)
        listRow[i].destroy()
        listLabel[i].destroy()
    gaussianBtn.destroy()
    jordanBtn.destroy()

    return mat

def show_results(ge):
    global display_solution
    global display_steps
    solution = ge.solve()
    steps = ge.steps
    display_steps = Label(second_frame, text=steps, font=('cairo', 18))
    display_steps.pack()
    if solution.any():
        ge.get_result(solution)
        display_solution = Label(second_frame, text=ge.solution, font=('cairo', 18))
        display_solution.pack()

def jord():
    global mat
    global display_solution
    global display_steps
    global btn_jordan

    ge = GaussJordanElimination(casting_float(mat))
    display_solution.destroy()
    display_steps.destroy()
    btn_jordan.destroy()
    show_results(ge)

def gaussianEle():
    global btn_jordan
    ge = GaussianElimination(casting_float(destroy_and_return()))
    show_results(ge)
    btn_jordan = Button(text='gaussian jordan elimination', command=jord, font=('cairo', 15))
    btn_jordan.pack()

def gauss():
    global mat
    global display_solution
    global display_steps
    global btn_gaussian

    ge = GaussianElimination(casting_float(mat))
    display_solution.destroy()
    display_steps.destroy()
    btn_gaussian.destroy()
    show_results(ge)

def jordanEle():
    global btn_gaussian
    ge = GaussJordanElimination(casting_float(destroy_and_return()))
    show_results(ge)
    btn_gaussian = Button(text='gaussian Elimnation', command=gauss, font=('cairo', 15))
    btn_gaussian.pack()

def enter():
    global gaussianBtn
    global jordanBtn
    global listRow
    global listLabel

    nRow = int(numUnknownEntry.get())
    numUnknown.destroy()
    numUnknownEntry.destroy()
    btnForm1.destroy()
    Y = 50
    listRow = []
    listLabel = []

    for i in range(nRow):
        row = Label(text=f'Enter Row{i + 1} (separated with spaces):')
        listLabel.append(row)
        row.place(x=20, y=Y)
        rowEntry = Entry(textvariable=row, width=12, font=('Verdana', 14))
        rowEntry.place(x=270, y=Y)
        Y += 50
        listRow.append(rowEntry)
        if i == nRow - 1:
            gaussianBtn = Button(text='Gaussian Elimnaition', command=gaussianEle)
            gaussianBtn.place(x=100, y=Y)
            jordanBtn = Button(text='Gaussian Jordan', command=jordanEle)
            jordanBtn.place(x=100, y=Y + 50)


btnForm1 = Button(text='ok!', command=enter)
btnForm1.place(x=350, y=55)

screen.mainloop()