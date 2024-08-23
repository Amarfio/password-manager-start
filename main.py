from tkinter import *
from tkinter import messagebox
import random
import json

import pyperclip
from pyperclip import copy
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():

    data = {}
    try:

        #get the contents of the data file
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)

        #get the name of the website
        website = website_textbox.get()

        #details of website
        details = {}
        for key, value in data.items():
            # print(key, value)
            if key == website:
                print(value)
                email_textbox.delete(0, 'end')
                email_textbox.insert(0, value['email'])
                password_textbox.delete(0, 'end')
                password_textbox.insert(0, value['password'])

                details = value
        #if name of the website does not match the details display the result to the user
        if details != {}:
            messagebox.showinfo(title=website, message=f"Email: {details['email']} \nPassword: {details['password']}")
        else:
            messagebox.showinfo(title=website, message="No details for the website exists")
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="Data file not found")
    # else:
    #     messagebox.showerror(title="Oops", message="An error occurred, kindly contact the developer")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 6)
    nr_numbers = random.randint(2, 6)

    # password_list = []

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    pass_letters = [random.choice(letters) for _ in range(nr_letters)]

    pass_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    pass_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list = pass_letters + pass_symbols + pass_numbers

    random.shuffle(password_list)

    print(password_list)
    password = "".join(password_list)
    copy(password)

    # print(f"Your password is: {password}")
    password_textbox.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # get all the values for the textboxes

    # check and focus on the empty textboxes
    if website_textbox.get() == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
        website_textbox.focus()
    elif password_textbox.get() == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
        password_textbox.focus()

    else:
        #     is_ok = messagebox.askokcancel(title=website_textbox.get(), message=f"These are the details entered: \nEmail:{email_textbox.get()}"
        #                                                                 f"\nPassword: {password_textbox.get()}"
        #                                                                 f"\nIs ito ok to save?")
        #     if is_ok:
        # and save them into file called saved_passwords.txt
        new_data = {
            website_textbox.get(): {
                "email": email_textbox.get(),
                "password": password_textbox.get()
            }
        }
        try:
            # print(new_data)
            with open("data.json", mode="r") as file:
                # reading old data
                data = json.load(file)


        except FileNotFoundError:
            # print(new_data)
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, index=4)

        else:
            print(new_data)
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
                # print(data)
                #     # for word in password_details:
                #     file.write(f"{website_textbox.get()} | {email_textbox.get()} | {password_textbox.get()}")
                #     file.write("\n")
                # check the mail merge to write to the file
        finally:
            website_textbox.delete(0, 'end')
            password_textbox.delete(0, 'end')
            # print(password_details)
            # print("Password saved successfully!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# draw the picture in the window
passImgCanvas = Canvas(width=200, height=200)
pass_logo_image = PhotoImage(file="logo.png")
passImgCanvas.create_image(100, 100, image=pass_logo_image)
passImgCanvas.grid(row=0, column=1)

# website lable
website_label = Label(text="Website:", width=15)
website_label.grid(row=1, column=0)

# website textbox
website_textbox = Entry(width=21)
website_textbox.focus()
website_textbox.grid(row=1, column=1)

# search_button
search_button = Button(text="Search", width=30, command=find_password)
search_button.grid(row=1, column=2)
# email label
email_label = Label(text="Email/Username:", width=15)
email_label.grid(row=2, column=0)

# email textbox
email_textbox = Entry(width=55)
email_textbox.insert(0, "joshuaamarfio1@gmail.com")
email_textbox.grid(row=2, column=1, columnspan=2)

# password label
password_label = Label(text="Password:", width=15)
password_label.grid(row=3, column=0)

# password textbox
password_textbox = Entry(width=21)
password_textbox.grid(column=1, row=3)

# generate pass button
generate_pass_button = Button(text="Generate Password", command=generate_password, width=30)
generate_pass_button.grid(row=3, column=2)

# add button
add_button = Button(text="Add", width=51, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
