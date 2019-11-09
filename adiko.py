from tkinter import *

root = Tk()
lis= []

def summa():
    lis.append(int(Entry1.get()))
    lis.append("+")
    Entry1.delete(0, END)

def difference():
    lis.append(int(Entry1.get()))
    lis.append("-")
    Entry1.delete(0, END)
def multiplication():
    lis.append(int(Entry1.get()))
    lis.append("*")
    Entry1.delete(0, END)
def division():
    lis.append(int(Entry1.get()))
    lis.append("/")
    Entry1.delete(0, END)


def vivod():
    lis.append(int(Entry1.get()))
    if lis[1]=="+":
        summ=lis[0] + lis[2]
        Entry1.delete(0, END)
        Entry1.insert(0, summ)
    elif lis[1]=="-":
        diff = lis[0] - lis[2]
        Entry1.delete(0, END)
        Entry1.insert(0, diff)
    elif lis[1]=="*":
        mult=lis[0] * lis[2]
        Entry1.delete(0, END)
        Entry1.insert(0, mult)
    else:
        div = lis[0] / lis[2]
        Entry1.delete(0, END)
        Entry1.insert(0, div)

def dellit():
    lis.clear()
    Entry1.delete(0, END)
    # Entry1.insert(0, "")


Entry1=Entry(root,width=18,font='Arial 16')
Entry1.grid(row=0, column=0, columnspan=5)

plus=Button(root,text="+", command=summa, width=3,height=2,bg='black',fg='white')
plus.grid(row=1, column=1, sticky=W+E)

minys=Button(root,text="-", command=difference, width=3,height=2,bg='black',fg='white')
minys.grid(row=1, column=2, sticky=W+E)

zvezdochka=Button(root,text="*", command=multiplication, width=3,height=2,bg='black',fg='white')
zvezdochka.grid(row=1, column=3, sticky=W+E)

slesh=Button(root,text="/", command=division, width=3,height=2,bg='black',fg='white')
slesh.grid(row=1, column=4, sticky=W+E)

ravno=Button(root,text="=", command=vivod, width=3,height=2,bg='black',fg='white')
ravno.grid(row=2, column=4, rowspan=3, sticky=W+E+N+S)

dell=Button(root,text="c", command=dellit, width=3,height=2,bg='black',fg='white')
dell.grid(row=1, column=0, sticky=W+E)

but1=Button(root,text="1", width=3,height=2,bg='black',fg='white', command=lambda: Entry1.insert(END, 1))
but1.grid(row=2, column=0, sticky=W+E)

but2=Button(root,text="2", width=3,height=2,bg='black',fg='white',command=lambda: Entry1.insert(END, 2))
but2.grid(row=2, column=1, sticky=W+E)

but3=Button(root,text="3", width=3,height=2,bg='black',fg='white',command=lambda: Entry1.insert(END, 3))
but3.grid(row=2, column=2, sticky=W+E)

but4=Button(root,text="4", width=3,height=2,bg='black',fg='white',command=lambda: Entry1.insert(END, 4))
but4.grid(row=2, column=3, sticky=W+E)

but5=Button(root,text="5", width=3,height=2,bg='black',fg='white',command=lambda: Entry1.insert(END, 5))
but5.grid(row=3, column=0, sticky=W+E)

but6=Button(root,text="6", width=3,height=2,bg='black',fg='white',command=lambda: Entry1.insert(END, 6))
but6.grid(row=3, column=1, sticky=W+E)

but7=Button(root,text="7", width=3,height=2,bg='black',fg='white',command=lambda: Entry1.insert(END, 7))
but7.grid(row=3, column=2, sticky=W+E)

but8=Button(root,text="8", width=3,height=2,bg='black',fg='white',command=lambda: Entry1.insert(END, 8))
but8.grid(row=3, column=3, sticky=W+E)

but9=Button(root,text="9", width=3,height=2,bg='black',fg='white',command=lambda: Entry1.insert(END, 9))
but9.grid(row=4, column=0, sticky=W+E)

but10=Button(root,text="0", width=3,height=2,bg='black',fg='white',command=lambda: Entry1.insert(END, 0))
but10.grid(row=4, column=1,columnspan=3, sticky=W+E)

root.mainloop()
