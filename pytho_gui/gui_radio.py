from tkinter import *

def sel():
    selection = "선택 항목 :" + str(var.get())
    label_a.config(text=selection)
app = Tk()
label_q = Label(app, text="1. 가장 배우기 쉬운 언어는?")
label_q.pack()

# 정수형 변수
var = IntVar()
Radiobutton(app, text="python", variable=var, value=1, command=sel).pack(anchor=W)
Radiobutton(app, text="java", variable=var, value=2, command=sel).pack(anchor=W)
Radiobutton(app, text="C", variable=var, value=3, command=sel).pack(anchor=W)
label_a = Label(app, text="")
label_a.pack()
app.mainloop()
