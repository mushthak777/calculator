from tkinter import*

def button_press(num):
    global equation_text
    
    equation_text=equation_text+str(num)
    
    equation_label.set(equation_text)

def equals():
    try:
        global equation_text
        total=str(eval(equation_text))
        equation_label.set(total)
        equation_text=total
    except ZeroDivisionError:
        equation_label.set("arithamatic error")
        equation_text=""
    except SyntaxError:
        equation_label.set("syntax error")
        equation_text=""

def clear():
    global equation_text
    equation_label.set("")
    equation_text=""

window=Tk()

window.title("Mushthak calculator ")
window.geometry("500x500")


equation_text=""

equation_label=StringVar()

label=Label(window,textvariable=equation_label,font=('consolas',20),bg="white",width=24,height=2)
label.pack()

fream=Frame(window)
fream.pack()

button1=Button(fream,text=1,height=4,width=9,font=35,command=lambda:button_press(1))
button1.grid(row=0,column=0)

button2=Button(fream,text=2,height=4,width=9,font=35,command=lambda:button_press(2))
button2.grid(row=0,column=1)

button3=Button(fream,text=3,height=4,width=9,font=35,command=lambda:button_press(3))
button3.grid(row=0,column=2)

button4=Button(fream,text=4,height=4,width=9,font=35,command=lambda:button_press(4))
button4.grid(row=1,column=0)

button5=Button(fream,text=5,height=4,width=9,font=35,command=lambda:button_press(5))
button5.grid(row=1,column=1)

button6=Button(fream,text=6,height=4,width=9,font=35,command=lambda:button_press(6))
button6.grid(row=1,column=2)

button7=Button(fream,text=7,height=4,width=9,font=35,command=lambda:button_press(7))
button7.grid(row=2,column=0)

button8=Button(fream,text=8,height=4,width=9,font=35,command=lambda:button_press(8))
button8.grid(row=2,column=1)

button9=Button(fream,text=9,height=4,width=9,font=35,command=lambda:button_press(9))
button9.grid(row=2,column=2)

button0=Button(fream,text=0,height=4,width=9,font=35,command=lambda:button_press(0))
button0.grid(row=3,column=1)

plus=Button(fream,text='+',height=4,width=9,font=35,command=lambda:button_press('+'))
plus.grid(row=0,column=3)

minus=Button(fream,text='-',height=4,width=9,font=35,command=lambda:button_press('-'))
minus.grid(row=1,column=3)

multiply=Button(fream,text='*',height=4,width=9,font=35,command=lambda:button_press('*'))
multiply.grid(row=2,column=3)

divided=Button(fream,text='/',height=4,width=9,font=35,command=lambda:button_press('/'))
divided.grid(row=3,column=3)

equal=Button(fream,text='=',height=4,width=9,font=35,command=equals)
equal.grid(row=3,column=2)

decimal=Button(fream,text='.',height=4,width=9,font=35,command=lambda:button_press('.'))
decimal.grid(row=3,column=0)

clear=Button(window,text='clear',height=4,width=9,font=35,command=clear)
clear.pack()

window.mainloop()