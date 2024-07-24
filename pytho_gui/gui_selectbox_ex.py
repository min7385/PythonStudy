from tkinter import *

app = Tk()
# title
app.title("환율 계산기")
# size
app.geometry("500x500")
# Label (단순 텍스트 출력)
lbl_amount = Label(app, text="Amount:")
lbl_amount.grid(row=1, column=1) # row는 행, column은 열
# Entry (입력창)
txt = Entry(app)
txt.grid(row=1, column=2)
# 문제 출력
lbl_from = Label(app, text="From:")
lbl_from.pack()

app.mainloop()

# 너도 미완성