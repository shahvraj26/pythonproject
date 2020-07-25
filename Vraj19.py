from tkinter import *
import random
import time
import sys

Tops2 = Tk()
Tops2.title('Vraj Calculator')

text_Input = StringVar()
operator =""

localtime=time.asctime(time.localtime(time.time()))

txtDisplay2 = Entry(Tops2, fg='white', font=('arial', 30,'bold'), text = '7', bd=0, insertwidth=0, bg = 'Red', justify='center')
txtDisplay2.grid(columnspan=6)
txtDisplay2.insert(END, "Vraj's Calculator",)

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=''
    text_Input.set('')

def btnEqualInput():
    global operator
    sumup= str(eval(operator))
    text_Input.set(sumup)
    operator = sumup
    return operator.func(*args)
    operator = ''

def btnBackDisplay():
    global operator
    print(operator)
    o_len=len(operator)
    operator=operator[0:o_len-1]
    text_Input.set(operator)

text_Input.set('0')

txtDisplay = Entry(Tops2,font=('arial', 20,'bold'),textvariable=text_Input, bd=30, insertwidth=8,
                   bg='Grey', justify='right')

txtDisplay.grid(columnspan=5)

btn7=Button(Tops2,padx=17,pady=17,bd=9, fg='white', font=('arial', 20,'bold'),
            text = '7', bg='red', command=lambda:btnClick(7)).grid(row=2,column=0)

btn8=Button(Tops2,padx=17,pady=17,bd=9, fg='white', font=('arial', 20,'bold'),
            text = '8', bg='green', command=lambda:btnClick(8)).grid(row=2,column=1)

btn9=Button(Tops2,padx=17,pady=17,bd=9, fg='white', font=('arial', 20,'bold'),
            text = '9', bg='grey', command=lambda:btnClick(9)).grid(row=2,column=2)

Addition=Button(Tops2,padx=17,pady=17,bd=9, fg='white', font=('arial', 20,'bold'),
            text ='+', bg='blue', command=lambda:btnClick('+')).grid(row=2,column=3)

btn4=Button(Tops2,padx=17,pady=17,bd=9, fg='white', font=('arial', 20,'bold'),
            text = '4', bg='red', command=lambda:btnClick(4)).grid(row=3,column=0)

btn5=Button(Tops2,padx=17,pady=17,bd=9, fg='white', font=('arial', 20,'bold'),
            text = '5', bg='green', command=lambda:btnClick(5)).grid(row=3,column=1)

btn6=Button(Tops2,padx=17,pady=17,bd=9, fg='white', font=('arial', 20,'bold'),
            text = '6', bg='grey', command=lambda:btnClick(6)).grid(row=3,column=2)

Subtraction=Button(Tops2,padx=19,pady=19,bd=9, fg='white', font=('arial', 20,'bold'),
            text ='-', bg='blue', command=lambda:btnClick('-')).grid(row=3,column=3)

btn1=Button(Tops2,padx=17,pady=17,bd=9, fg='white', font=('arial', 20,'bold'),
            text = '1', bg='red', command=lambda:btnClick(1)).grid(row=4,column=0)

btn2=Button(Tops2,padx=17,pady=17,bd=9, fg='white', font=('arial', 20,'bold'),
            text = '2', bg='green', command=lambda:btnClick(2)).grid(row=4,column=1)

btn3=Button(Tops2,padx=17,pady=17,bd=9, fg='white', font=('arial', 20,'bold'),
            text = '3', bg='grey', command=lambda:btnClick(3)).grid(row=4,column=2)

Multiply=Button(Tops2,padx=18,pady=19,bd=9, fg='white', font=('arial', 20,'bold'),
            text ='*', bg='blue', command=lambda:btnClick('*')).grid(row=4,column=3)

btn0=Button(Tops2,padx=17,pady=19,bd=9, fg='white', font=('arial', 20,'bold'),
            text = '0', bg='red', command=lambda:btnClick(0)).grid(row=5,column=0)

btnC=Button(Tops2,padx=17,pady=17,bd=9, fg='white', font=('arial', 20,'bold'),
            text = 'C', bg='green', command=btnClearDisplay).grid(row=5,column=1)

btnEquals=Button(Tops2,padx=17,pady=17,bd=9, fg='white', font=('arial', 20,'bold'),
            text = '=', bg='grey', command=btnEqualInput).grid(row=5,column=2)

Division=Button(Tops2,padx=19,pady=19,bd=9, fg='white', font=('arial', 20,'bold'),
            text ='/', bg='blue', command=lambda:btnClick('/')).grid(row=5,column=3)

Power=Button(Tops2,padx=25,pady=17,bd=9, fg='white', font=('arial', 20,'bold'),
            text ='^', bg='Black', command=lambda:btnClick('**')).grid(row=2,column=4)

Dot=Button(Tops2,padx=29,pady=19,bd=8, fg='white', font=('arial', 20,'bold'),
            text ='.', bg='Black', command=lambda:btnClick('.')).grid(row=3,column=4)

btnCE=Button(Tops2,padx=14,pady=17,bd=9, fg='white', font=('arial', 20,'bold'),
            text = 'CE', bg='Black', command=btnClearDisplay).grid(row=4,column=4)

btnBack=Button(Tops2,padx=14,pady=17,bd=9, fg='white', font=('arial', 20,'bold'),
            text = '<=', bg='Black', command=btnBackDisplay).grid(row=5,column=4)


Tops2.resizable(False,False)

Tops2.mainloop()
