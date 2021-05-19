from tkinter import *
from tkinter import messagebox, Entry
import pyperclip
import json
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = site_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0:
        messagebox.askokcancel(title="oops", message="Please, don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            site_entry.delete(0, END)
            pass_entry.delete(0, END)


def find_password():
    website = site_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="NOPE NOPE NOPE")
    else:
        if website in data:
            messagebox.askokcancel(title={website},
                                   message=f"found it site: {website}, passwprd: {data[website]['password']}")
        else:
            messagebox.askokcancel(title="oops", message=f"nope")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)

canvas.grid(column=1, row=0)
# Labels
site_label = Label(text="Website", width=21)
site_label.grid(column=0, row=1)

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)

pass_label = Label(text="Password")
pass_label.grid(column=0, row=3)

# Entries
site_entry = Entry(width=36)
site_entry.grid(column=1, columnspan=2, row=1)
site_entry.focus()

email_entry = Entry(width=36)
email_entry.grid(column=1, columnspan=2, row=2)
email_entry.insert(0, "fuck@your.self")

pass_entry: Entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", width=15, command=generate_pass)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, columnspan=2, row=4)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)
window.mainloop()
