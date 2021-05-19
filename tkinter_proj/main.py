from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100,pady=200)

# Label
my_label = Label(text="I am Label", font=("Arial", 24, "italic"))
# my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.place(x=100, y=200)
my_label.grid(column=0,row=0)

# Button
def button_clicked():
    smth = input.get()
    my_label["text"] = smth


button = Button(text="lick Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)
# Entry
button = Button(text="Click On Me", command=button_clicked)
button.grid(column=2, row=0)

input = Entry(width=10)
# input.pack()
input.grid(column=3,row=2)


window.mainloop()
