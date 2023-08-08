from tkinter import*
from tkinter import ttk

Window = Tk()
Window.geometry("500x500")
Window.title("Brototype")
Window.configure(bg="red")


def hello():
    print("Button clicked")

button1 = Button(text="1",command=hello)
button2 = Button(text="2",command=hello)
button3 = Button(text="3",command=hello)
button4 = Button(text="4",command=hello)
button5 = Button(text="5",command=hello)
button6 = Button(text="6",command=hello)
button7 = Button(text="7",command=hello)
button8 = Button(text="8",command=hello)
button9 = Button(text="9",command=hello)
button0 = Button(text="0",command=hello)



button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)

button4.grid(row=1,column=0)
button5.grid(row=1,column=1)
button6.grid(row=1,column=2)

button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)






Window.mainloop()