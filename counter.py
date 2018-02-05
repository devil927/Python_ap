from tkinter import *
counter=0
def counter_label(label):
    def count():
        global counter
        counter=counter+1
        label.config(text=str(counter))
        label.after(1000,count)
    count()
def s():
    save=str(counter)
    r.destroy()
    r1=Tk()
    l=Label(r1,text="Counted :",fg="black").pack(side="left")
    label=Label(r1,text=save,fg="dark green").pack()
    
r=Tk()
r.title("Counter")
r.geometry("200x70+200+200")
l=Label(r,text="Counter :",fg="black").pack()
label=Label(r,fg="dark green")
label.pack()
counter_label(label)
b=Button(r,text="Stop",bd=1,fg="red",command=s)
b.pack(fill='x')
r.mainloop()
