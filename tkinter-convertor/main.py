from tkinter import *

window = Tk()
window.title("Euro to rub ")
window.minsize(width=100, height=100)
window.config(padx=10, pady=20)

input_field = Entry(width=15)
input_field.grid(column=1, row=0)

euro = Label(text="Euro", font=("Arial", 14, "italic"))
euro.grid(column=2, row=0)

equal = Label(text="is equal to", font=("Arial", 14, "italic"))
equal.grid(column=0, row=1)

val_in_eur = Label(text="", font=("Arial", 14, "italic"))
val_in_eur.grid(column=1, row=1)

rub = Label(text="Rub", font=("Arial", 14, "italic"))
rub.grid(column=2, row=1)

def button_clicked():
    amn = int(input_field.get())
    val_in_eur['text'] = round(amn * 90.43)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()


