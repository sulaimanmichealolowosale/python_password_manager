from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip


# -----------------------------------GENERATE PASSWORD-----------------------------------

def generate_password():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']

    letters_list = [choice(letters) for char in range(randint(8, 10))]
    numbers_list = [choice(numbers) for char in range(randint(2, 4))]
    symbols_list = [choice(symbols) for char in range(randint(2, 4))]

    password_list = letters_list + numbers_list+symbols_list

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# -----------------------------------SAVE PASSWORD-----------------------------------

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or password == "" or email == "":
        messagebox.showinfo(
            title="Oops", message="Hey you left either the website, email, or password field empty \n\nPlease check again")
    else:

        is_okay = messagebox.askokcancel(
            title=website, message=f"These are the details entered: \n\nEmail: {email} \n\nPassword: {password}\n\nDo you want to save? ")

        if is_okay:
            with open("password.txt", "a") as password_file:
                password_file.write(
                    f"Website: {website} || email: {email} || password: {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# -----------------------------------USER INTERFACE-----------------------------------
window = Tk()
window.title("Passsword Manager")
window.config(padx=70, pady=70)

# ------------------IMAGE--------------------
canvas = Canvas(height=300, width=300)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=logo_image)
canvas.grid(row=0, column=1)


# ---------------------LABELS-----------------
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)


# ------------------ENTRIES-------------------
website_entry = Entry(width=68)
email_entry = Entry(width=68)
password_entry = Entry(width=50)

website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry.grid(row=2, column=1, columnspan=2, pady=3)
email_entry.insert(0, "mike@gmail.com")

password_entry.grid(row=3, column=1)

# --------------------BUTTONS------------------
generate_password_button = Button(
    text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=58, command=save)

generate_password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
