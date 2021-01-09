from tkinter import *

def btn_click(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btn_clear():
    global operator
    operator=""
    text_Input.set("")

def btn_equal():
    global operator
    op_val=str(eval(operator))
    text_Input.set(op_val)
    operator=""

cal = Tk()
cal.title("Calculator")
operator=""
text_Input = StringVar()

txtDisplay=Entry(cal,font=('arial',20,"bold"),
                 textvariable=text_Input,bd=30,insertwidth=4,bg="powder blue",justify="right").grid(columnspan=4)

# for 7,8,9,=
btn7=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,"bold"),
            text="7",command=lambda:btn_click(7),bg="powder blue").grid(row=1,column=0)
btn8=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,"bold"),
            text="8",command=lambda:btn_click(8),bg="powder blue").grid(row=1,column=1)
btn9=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,"bold"),
            text="9",command=lambda:btn_click(9),bg="powder blue").grid(row=1,column=2)
btn_equal=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,"bold"),
            text="=",command=btn_equal,bg="powder blue").grid(row=1,column=3)

#for 4,5,6,+
btn4=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,"bold"),
            text="4",command=lambda:btn_click(4),bg="powder blue").grid(row=2,column=0)
btn5=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,"bold"),
            text="5",command=lambda:btn_click(5),bg="powder blue").grid(row=2,column=1)
btn6=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,"bold"),
            text="6",command=lambda:btn_click(6),bg="powder blue").grid(row=2,column=2)
btn_plus=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,"bold"),
            text="+",command=lambda:btn_click("+"),bg="powder blue").grid(row=2,column=3)

#for 1,2,3,-
btn1=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,"bold"),
            text="1",command=lambda:btn_click(1),bg="powder blue").grid(row=3,column=0)
btn2=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,"bold"),
            text="2",command=lambda:btn_click(2),bg="powder blue").grid(row=3,column=1)
btn3=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,"bold"),
            text="3",command=lambda:btn_click(3),bg="powder blue").grid(row=3,column=2)
btn_sub=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,"bold"),
            text="-",command=lambda:btn_click("-"),bg="powder blue").grid(row=3,column=3)
#for 0,%,/,x
btn0=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,"bold"),
            text="0",command=lambda:btn_click(0),bg="powder blue").grid(row=4,column=0)
btn_clr=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,"bold"),
            text="C",command=lambda:btn_clear(),bg="powder blue").grid(row=4,column=1)
btn_div=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,"bold"),
            text="/",command=lambda:btn_click("/"),bg="powder blue").grid(row=4,column=2)
btn_mul=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,"bold"),
            text="X",command=lambda:btn_click("*"),bg="powder blue").grid(row=4,column=3)


cal.mainloop()