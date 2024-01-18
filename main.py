from tkinter import *

BG = "white"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50, bg=BG)

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
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(bg=BG, width=43)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(bg=BG, width=24)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", bg=BG)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", bg=BG, width=36)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()

