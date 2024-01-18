from tkinter import *

BG = "white"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.configure(padx=20, pady=20, bg=BG)

canvas = Canvas(height=200, width=200, bg=BG, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website", bg=BG, anchor="e")
website_label.grid(column=0, row=1)


window.mainloop()