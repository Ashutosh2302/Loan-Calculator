from tkinter import *
fields=("Loan Amount","No of Installments","Rate of Interest","Installment")
def makeform(root,fields):
    entries={}
    for field in fields:
        row=Frame(root)
        l1=Label(row,text=field+": ")
        e1=Entry(row)
        e1.insert(0,"0")
        row.pack(side=TOP,fill=X,padx=5,pady=5)
        l1.pack(side=LEFT)
        e1.pack(side=RIGHT)
        entries[field]=e1
    entries[field].configure(state=DISABLED)
    return entries
def calculate_installments(entries):
     p=float(entries[fields[0]].get())
     n=float(entries[fields[1]].get())
     r=(float(entries[fields[2]].get())/100)/12
     i=p*r*(1+r)**n/((1+r)**n -1)
     i=("%8.2f"%i).strip()

     entries[fields[3]].config(state=NORMAL)
     entries[fields[3]].delete(0, END)
     entries[fields[3]].insert(0,i)
     entries[fields[3]].config(state=DISABLED)

def reset(entries):
    for field in fields:
        entries[field].delete(0, END)
        entries[field].insert(0,"0")
    entries[field].config(state=NORMAL)
    entries[field].delete(0, END)
    entries[field].insert(0, "0")
    entries[field].config(state=DISABLED)

def quit():
    root.destroy()

if __name__=="__main__":
    root=Tk()
    root.title("Loan Calculator")
    root.geometry("300x200")
    root.wm_maxsize(width=300,height=200)
    root.wm_minsize(width=300, height=200)
    ents=makeform(root,fields)
    b1=Button(root,text="Calculate Installment",command=(lambda e=ents:calculate_installments(e)))
    b1.pack(side=LEFT,padx=5,pady=5)
    b2=Button(root,text="Exit",command=quit)
    b2.pack(side=LEFT,padx=5,pady=5)
    b3=Button(root,text="Reset",command=(lambda e=ents:reset(e)))
    b3.pack(side=RIGHT,padx=5,pady=5)
    root.mainloop()