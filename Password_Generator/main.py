from tkinter import *
from tkinter import messagebox
import pyperclip

from numpy.random import randint, shuffle, choice


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    my_password = ''.join(password_list)
    password_provided.insert(0,my_password)
    pyperclip.copy(my_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_passwords():
    final_website_name = website_name.get()
    final_username = user_name.get()
    final_password = password_provided.get()

    if len(final_website_name) < 1 or len(final_password) < 1:
        messagebox.showinfo(title="Oops", message="Please Don't Leave any field's empty!")
    else:
        is_ok = messagebox.askokcancel(title=final_website_name,
                                       message=f"These are the Details Entered:\nEmail: {final_username}\nPassword: {final_password}")

        with open("records.txt", "a") as f:
            if is_ok:
                f.write(f"{final_website_name} | {final_username} | {final_password}\n")
                website_name.delete(0, 'end')
                password_provided.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website = Label(text="Website: ", padx=5, pady=5)
website.grid(row=1, column=0)

website_name = Entry(width=48)
website_name.grid(row=1, column=1, columnspan=2)
website_name.focus()

user = Label(text="Email/Username: ", padx=5, pady=5)
user.grid(row=2, column=0)

user_name = Entry(width=48)
user_name.grid(row=2, column=1, columnspan=2)
user_name.insert(0, "amrutareddy93@gmail.com")

password = Label(text="Password: ", padx=5, pady=5)
password.grid(row=3, column=0)

password_provided = Entry(width=30)
password_provided.grid(row=3, column=1)

generate_password = Button(text="Generate Password",command=password_generator)
generate_password.grid(row=3, column=2)

add = Button(text="Add", width=36, command=add_passwords)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
