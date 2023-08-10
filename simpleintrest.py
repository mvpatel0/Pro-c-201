from tkinter import *
window=Tk()

window.title('Simple Intrest Calculator')
window.geometry('380x400')
window.configure(bg='#2D6496')

def calculate():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    intrest = round(i,2)
    outputmessage=Label(result_frame,text=" your simple intrest is "+str(i), bg = "#2D6496", font=("Calibri", 12), width=42)
    outputmessage.place(x=20,y=40)
    outputmessage.pack()


app_label=Label(window, text="Simple Intrest Calculator", fg = "black", bg = "#2D6496", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

principle_label = Label(window,text="Enter principle",fg="black",bg="#2D6496",font=("Calibri",12))
principle_label.place(x=20,y=140)

principle= Entry(window,text="",bd=2,width=15)
principle.place(x=150,y=142)

rate_label = Label(window,text="rate (in %)",fg="black",bg="#2D6496",font=("Calibri",12))
rate_label.place(x=20,y=185)

rate = Entry(window,text="",bd=2,width=15)
rate.place(x=150,y=187)

time_label = Label(window,text="time(in years)",fg="black",bg="#2D6496",font=("Calibri",12))
time_label.place(x=20,y=230)

time = Entry(window,text="",bd=2,width=15)
time.place(x=150,y=232)

calculate_button = Button(window , text="calculate", fg="black", bg="#31586F",bd=4,command=calculate)
calculate_button.place(x=20,y=280)

result_frame = LabelFrame(window,text="Result", bg = "#2D6496", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "#2D6496", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()


window.mainloop()