from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

DATA_FILE_PATH = None

BG = "white"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


def generate_password():
    list_letters = [random.choice(letters) for _ in range(nr_letters)]
    symbols_letters = [random.choice(symbols) for _ in range(nr_symbols)]
    number_letters = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = list_letters + symbols_letters + number_letters
    random.shuffle(password_list)
    password = "".join(password_list)
    return password


def new_password_to_password_entry():
    password_entry.delete(0, END)
    password_entry.insert(0, generate_password())
    pyperclip.copy(f"{password_entry.get()}")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def check_and_log_data():
    website = str(website_entry.get())
    email = str(email_entry.get())
    password = str(password_entry.get())

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(website) == 0:
        messagebox.showwarning(title="Warning", message=f"Not all data has been completed!")
    else:
        try:
            with open("users_data.json", "r") as f:
                data = json.load(f)
                data.update(new_data)
            with open("users_data.json", "w") as f:
                json.dump(data, f, indent=4)

        except FileNotFoundError:
            with open("users_data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        finally:
            password_entry.delete(0, END)
            website_entry.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50, bg=BG)
window.configure(highlightthickness=0)

canvas = Canvas(height=200, width=200, bg=BG, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg=BG)
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg=BG)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg=BG)
password_label.grid(column=0, row=3)

website_entry = Entry(bg=BG, width=43)
website_entry.grid(column=1, row=1, columnspan=2, sticky="nsew")
website_entry.focus()

email_entry = Entry(bg=BG, width=43)
email_entry.grid(column=1, row=2, columnspan=2, sticky="nsew")
email_entry.insert(0, "monika123@wp.pl")

password_entry = Entry(bg=BG, width=24)
password_entry.grid(column=1, row=3, sticky="nsew")

generate_password_button = Button(text="Generate Password", bg=BG, command=lambda: new_password_to_password_entry())
generate_password_button.grid(column=2, row=3, padx=0, sticky="nsew")

search_website = Button(text="Search", bg=BG, command=lambda: new_password_to_password_entry())
search_website.grid(column=2, row=1, padx=0, sticky="nsew")

add_button = Button(text="Add", bg=BG, width=36, command=lambda: check_and_log_data())
add_button.grid(column=1, row=4, columnspan=2, sticky="nsew")


window.mainloop()

