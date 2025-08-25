"""""
Program: NguyenU9AE
Author: Loc Nguyen
Last Date Modified: 04/13/2022

"""""
from tkinter import *
import math
print('')
print('')
names = input('Provided your name here: ')
print('Welcome', names + '!', 'to the programm.')

expression = ''


def press(num):
    global expression
    expression += str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ''
    except:
        equation.set('error')
        expression = ''


def clear():
    global expression
    expression = ''
    equation.set('')


if __name__ == '__main__':
    # create GUI window
    gui = Tk()

    # set background color
    gui.configure(background="light green")

    #
    gui.title = ('Calculator')

    # set the size of the window
    gui.geometry('450x250')

    #
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)

    # create and run Button
    button1 = Button(gui, text='1', fg='black', bg='grey',command=lambda: press(1), height=1, width=5)
    button1.grid(row=1, column=0)

    buttion2 = Button(gui, text='2', fg='black', bg='grey',command=lambda: press(2), height=1, width=5)
    buttion2.grid(row=1, column=1)

    buttion3 = Button(gui, text='3', fg='black', bg='grey',command=lambda: press(3), height=1, width=5)
    buttion3.grid(row=1, column=2)

    buttion4 = Button(gui, text='4', fg='black', bg='grey',command=lambda: press(4), height=1, width=5)
    buttion4.grid(row=2, column=0)

    buttion5 = Button(gui, text='5', fg='black', bg='grey',command=lambda: press(5), height=1, width=5)
    buttion5.grid(row=2, column=1)

    buttion6 = Button(gui, text='6', fg='black', bg='grey',command=lambda: press(6), height=1, width=5)
    buttion6.grid(row=2, column=2)

    buttion7 = Button(gui, text='7', fg='black', bg='grey',command=lambda: press(7), height=1, width=5)
    buttion7.grid(row=3, column=0)

    buttion8 = Button(gui, text='8', fg='black', bg='grey',command=lambda: press(8), height=1, width=5)
    buttion8.grid(row=3, column=1)

    buttion9 = Button(gui, text='9', fg='black', bg='grey',command=lambda: press(9), height=1, width=5)
    buttion9.grid(row=3, column=2)

    pluss = Button(gui, text='+', fg='black', bg='grey',command=lambda: press('+'), height=1, width=5)
    pluss.grid(row=1, column=4)

    minuss = Button(gui, text='-', fg='black', bg='grey',command=lambda: press('-'), height=1, width=5)
    minuss.grid(row=2, column=4)

    multiplyss = Button(gui, text='*', fg='black', bg='grey',command=lambda: press('*'), height=1, width=5)
    multiplyss.grid(row=3, column=4)

    dividess = Button(gui, text='/', fg='black', bg='grey',command=lambda: press('/'), height=1, width=5)
    dividess.grid(row=4, column=4)

    docss = Button(gui, text='.', fg='black', bg='grey',command=lambda: press('.'), height=1, width=5)
    docss.grid(row=4, column=0)

    zeross = Button(gui, text='0', fg='black', bg='grey',command=lambda: press(0), height=1, width=5)
    zeross.grid(row=4, column=1)

    equalss = Button(gui, text='=', fg='black', bg='grey',command=equalpress, height=1, width=5)
    equalss.grid(row=4, column=2)

    clearss = Button(gui, text='clear', fg='black', bg='grey',command=clear, height=1, width=5)
    clearss.grid(row=5, column=0)

    m = Button(gui, text='(', fg='black', bg='grey',command=lambda: press('('), height=1, width=5)
    m.grid(row=7, column=1) 
    n = Button(gui, text=')', fg='black', bg='grey',command=lambda: press(')'), height=1, width=5)
    n.grid(row=7, column=2)
    
    exps = Button(gui, text='EXP', fg='black', bg='grey',command=math.exp(1), height=1, width=5)
    exps.grid(row=5, column=1)
    
    sq = Button(gui, text='Sqrt', fg='black', bg='grey',command=math.sqrt(1), height=1, width=5)
    sq.grid(row=5, column=2)
    # start the GUI
    gui.mainloop()
