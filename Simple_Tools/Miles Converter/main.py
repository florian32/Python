# test2
from tkinter import *

window = Tk()
window.title("Conveersion")
window.minsize(width=500, height=500)
label = Label(text="input miles: ", font=("Arial", 24))
label.grid(row=0, column=0)

entry = Entry(width=30)
entry.grid(row=0, column=1)

second_label = Label(text="That is", font=("Arial", 24))
second_label.grid(row=1, column=0)

third_label = Label(text="0", font=("Arial", 24))
third_label.grid(row=1, column=1)

miles = Label(text="km", font=("Arial", 24))
miles.grid(row=1, column=2)


def conversion():
    third_label["text"] = int(entry.get()) * 1.609344


button = Button(text="Convert", command=conversion)
button.grid(row=2, column=1)

window.mainloop()
