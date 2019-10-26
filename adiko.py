from tkinter import *

root =Tk()

def summa():

    print (int(Entry1.get()) + int(Entry2.get()))

Entry1=Entry(root,width=10,font='Arial 16')
Entry1.pack()

Entry2=Entry(root,width=10,font='Arial 16')
Entry2.pack()

# Entry3=Entry(root,width=20,font='Arial 16')
# Entry3.pack()
fddfhsu = [Button().grid() for x in range(10)]

but=Button(root,text='сумма', command=summa)
but.pack()
root.mainloop()
