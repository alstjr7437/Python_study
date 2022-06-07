from tkinter import *
from tkinter import messagebox


def myFunc() :

    messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠")

window = Tk()
window.title("윈도우 창 연습")

button1 = Button(window, text="버튼1", command = myFunc())


label = Label(window, text="라벨")

button2 = Button(window, text="버튼2", command=window.destroy(),width=10,height=2)

button1.pack(side=LEFT)
label.pack()
button2.pack()

window.mainloop()