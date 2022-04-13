from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password generator project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(2, 3)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def search():
    website = entry_website.get()

    try:
        with open("password_data_file.json", mode="r") as data_file:
            # Reading old data
            data_search = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="File not found", message="No details for this website.")
    else:
        if website in data_search:
            email = data_search[website]["email"]
            password = data_search[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="No details", message="No details for this website.")


def save_password():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Empty fields", message="Please don't leave fields empty!")
    else:
        try:
            with open("password_data_file.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("password_data_file.json", mode="w") as data_file:
                # Saving updating data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("password_data_file.json", mode="w") as data_file:
                # Saving updating data
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("My Pass Generator")
window.config(padx=60, pady=60)


canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_photo)
canvas.grid(column=1, row=0)

# Labels

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

# Entries

entry_website = Entry(width=33)
entry_website.grid(column=1, row=1)
entry_website.focus()

entry_email = Entry(width=51)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, "ana.nitu1@yahoo.com")

entry_password = Entry(width=33)
entry_password.grid(column=1, row=3)

# Buttons

button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", width=42, highlightthickness=0, command=save_password)
button_add.grid(column=1, row=4, columnspan=2)

button_search = Button(text="Search", width=15, bg="#B2DFEE", command=search)
button_search.grid(column=2, row=1)

window.mainloop()
