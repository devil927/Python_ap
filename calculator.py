#                                          Import library
#===========================================================================================================
from tkinter import *
#                                          Button operation
#===========================================================================================================
# Display the input
def btnc(number):
    global operator
    operator=operator+str(number)
    text_str.set(operator)
# Clear Button
def btnclr():
    global operator
    operator=""
    text_str.set(operator)
# For Evaluation of the inputs
def btneval():
    global operator
    try:
        s=str(eval(operator))
        text_str.set(s)
    except:
        text_str.set("Syntax error")
    operator=""
#                                            Gui 
#===========================================================================================================
cal=Tk()
cal.title("Calculator")
cal.resizable(width=False,height=False)
text_str=StringVar()
text_inp=Entry(cal,font=('arial',20,'bold'),textvariable=text_str,bd=20,insertwidth=4,
               bg="powder blue",justify='right')
text_inp.grid(columnspan=4,rowspan=2)
operator=""
   
#                                         Buttons
#=============================================================================================================
bt7=Button(cal,text='7',font=('arial',20,'bold'),padx=15,pady=8,bd=8,fg="black",bg="powder blue",command=lambda:btnc(7)).grid(row=3,column=0) #Button 7
bt8=Button(cal,text='8',font=('arial',20,'bold'),padx=15,pady=8,bd=8,fg="black",bg="powder blue",command=lambda:btnc(8)).grid(row=3,column=1) #Button 8
bt9=Button(cal,text='9',font=('arial',20,'bold'),padx=15,pady=8,bd=8,fg="black",bg="powder blue",command=lambda:btnc(9)).grid(row=3,column=2) #Button 9
plus=Button(cal,text='+',font=('arial',20,'bold'),padx=15,pady=8,bd=8,fg="black",bg="powder blue",command=lambda:btnc("+")).grid(row=3,column=3)
#=============================================================================================================
bt4=Button(cal,text='4',font=('arial',20,'bold'),padx=15,bd=8,pady=8,fg="black",bg="powder blue",command=lambda:btnc(4)).grid(row=4,column=0) #Button 4
bt5=Button(cal,text='5',font=('arial',20,'bold'),padx=15,bd=8,pady=8,fg="black",bg="powder blue",command=lambda:btnc(5)).grid(row=4,column=1) #Button 5
bt6=Button(cal,text='6',font=('arial',20,'bold'),padx=15,bd=8,pady=8,fg="black",bg="powder blue",command=lambda:btnc(6)).grid(row=4,column=2) #Button 6
sub=Button(cal,text='- ',font=('arial',20,'bold'),padx=15,bd=9,pady=8,fg="black",bg="powder blue",command=lambda:btnc("-")).grid(row=4,column=3)
#=============================================================================================================
bt1=Button(cal,text='1',font=('arial',20,'bold'),padx=15,bd=8,pady=8,fg="black",bg="powder blue",command=lambda:btnc(1)).grid(row=5,column=0) #Button 1
bt2=Button(cal,text='2',font=('arial',20,'bold'),padx=15,bd=8,pady=8,fg="black",bg="powder blue",command=lambda:btnc(2)).grid(row=5,column=1) #Button 2
bt3=Button(cal,text='3',font=('arial',20,'bold'),padx=15,bd=8,pady=8,fg="black",bg="powder blue",command=lambda:btnc(3)).grid(row=5,column=2) #Button 3
multiply=Button(cal,text='X',font=('arial',20,'bold'),padx=15,pady=8,bd=8,fg="black",bg="powder blue",command=lambda:btnc("x")).grid(row=5,column=3)
#=============================================================================================================
remainder=Button(cal,text='%',font=('arial',20,'bold'),padx=15,bd=8,pady=8,fg="black",bg="powder blue",command=lambda:btnc("%")).grid(row=6,column=0)
bt12=Button(cal,text='0',font=('arial',20,'bold'),padx=15,pady=8,bd=8,fg="black",bg="powder blue",command=lambda:btnc(0)).grid(row=6,column=1)
dot=Button(cal,text='. ',font=('arial',20,'bold'),padx=15,bd=8,pady=8,fg="black",bg="powder blue",command=lambda:btnc(".")).grid(row=6,column=2)
div=Button(cal,text='/ ',font=('arial',20,'bold'),padx=15,bd=8,pady=8,fg="black",bg="powder blue",command=lambda:btnc("/")).grid(row=6,column=3)
#=============================================================================================================
clr=Button(cal,text='c',font=('arial',20,'bold'),padx=56,pady=8,bd=8,fg="black",bg="powder blue",command=btnclr).grid(row=2,column=0,columnspan=2)
equal=Button(cal,text='=',font=('arial',20,'bold'),padx=56,pady=8,bd=8,fg="black",bg="powder blue",command=btneval).grid(row=2,columnspan=2,column=2)
#================================================================================================================================= Button ends here
cal.mainloop()

