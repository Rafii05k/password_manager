from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for item in range(randint(6, 8))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers =[choice(numbers) for n in range(randint(2, 4))]
    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,  password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(password)==0 or len(website)==0:
        messagebox.showinfo(message="Hey, you left some fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"this is the detail u entered:\nwebsite:"
                                         f" {website}\n email: {email}\n password: {password}\n u wanna submit?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f" {website}   | {email}   |   {password}  \n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)
# create canvas
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# grid layout
# Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "someone@gmail.com")
password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)

# buttons
password_button = Button(text="Generate password", command=password_generator)
password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=30, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()