from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SEARCH JSON FILE ----------------------------#

def search():
    source = website_entry.get()
    user = user_entry.get()

    try:
        with open("data.json", "r") as datafile:  # read file
            data = json.load(datafile)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="File not created, fill in the blanks!")
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Oops", message="Decrypt the file first")
    else:
        with open("data.json", "r") as datafile:  # read file
            data = json.load(datafile)
            if source in data:
                user = data[source]["user"]
                password = data[source]["password"]
                messagebox.showinfo(title="Info", message=f"{source} User: {user}\npassword: {password}")
            else:
                messagebox.showinfo(title="Info", message="Entry not found")
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    source = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    # create dictionary for json
    newdata = {
        source: {
            "user": user,
            "password": password,
        }
    }

    if len(source) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try: #try this first, if file is not there go to ecpetion
            with open("data.json", "r") as datafile: # read file
                data = json.load(datafile)# json to retrieve from json file
        except FileNotFoundError: #if data file doesnt exist, create it
            with open("data.json", "w") as datafile:  # write file
                json.dump(newdata, datafile, indent=4) # write the updated info to file

        else: #otherwise if file does exist update the file with new info
            data.update(newdata)
            with open("data.json", "w") as datafile:  # write file
                json.dump(data, datafile, indent=4) # write the updated info to file
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
bg = PhotoImage(file="logo.png")
window.config(padx=50, pady=50,bg="black")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=bg)
canvas.configure(bg="blue")
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
user_entry = Entry(width=21)
user_entry.grid(row=2, column=1, columnspan=1)
user_entry.insert(0, "cm.eml@icloud.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search",width=10, command=search)
search_button.grid(row=1, column=2)


window.mainloop()