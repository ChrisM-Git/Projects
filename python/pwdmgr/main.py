from tkinter import *
from tkinter import messagebox as mb
from random import randint,shuffle,choice
import pyperclip
from cryptography.fernet import Fernet

def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("filekey.key", "wb") as key_file:
        key_file.write(key)
def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("filekey.key", "rb").read()
def encrypt():
    write_key()
    key = load_key()
    F = Fernet(key)
    with open("pwdmgrfile.txt", "rb") as pwdfile:
        filedata = pwdfile.read()
    encrypted = F.encrypt(filedata)
    with open("pwdmgrfile.txt", "wb") as pwdfile:
        pwdfile.write(encrypted)
    mb.showwarning(title="Encrpt", message=f"File has been encrypted")
def decrypt():
    key = load_key()
    f = Fernet(key)
    with open("pwdmgrfile.txt", "rb") as pwdfile:
        # read the encrypted data
        encrypted_data = pwdfile.read()
        # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open("pwdmgrfile.txt", "wb") as pwdfile:
        pwdfile.write(decrypted_data)
    mb.showwarning(title="Decrypt", message=f"Warning, File has been decrypted!")




PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pwdgen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    letterlist = [choice(letters) for _ in range(randint(8, 10))]
    symbollist = [choice(symbols) for _ in range(randint(2, 4))]
    numberlist = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letterlist + symbollist + numberlist

    shuffle(password_list)
    password = "".join(password_list)
    pwdent.insert(0, password)
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
#
#
def add():
    sourceinput = sourceent.get()
    userinput = userent.get()
    password = pwdent.get()

    if len(sourceinput) == 0 or len(userinput) == 0 or len(password) == 0:
        mb.showwarning(title=sourceinput,message=f"Please fill in all the fields")

    else:
        confirm = mb.askokcancel(title=sourceinput,message=f"These are the credentials entered:\n Username:{userinput} \npasword:{password} \n Ok to Save?")

        if confirm == True:
            with open("pwdmgrfile.txt", "a") as file:
                file.write(f"{sourceinput} '|' {userinput} '|' {password} \n")
        else:
            sourceent.delete(0, 'end')
            pwdent.delete(0, 'end')

    sourceent.delete(0, 'end')
    pwdent.delete(0, 'end')



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)
canvas = Canvas(window, width=200, height=200, bg="black")
# labels
source = Label(text = "Program / Site:", font=(FONT_NAME, 14,"bold"))
source.grid(column=0,row=1)
user = Label(text = "Username:", font=(FONT_NAME, 14,"bold"))
user.grid(row=2)
pwd = Label(text = "Password:", font=(FONT_NAME, 14,"bold"))
pwd.grid(row=3)

# logo
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1, row=0)

#entries
sourceent = Entry(width=20)
sourceent.grid(column=1,row=1) # use columnspan to stretch across 2 rows columnspan = 2
sourceent.focus()


userent = Entry(width=20)
userent.grid(column=1,row=2)
userent.insert(0, "cm.eml@icloud.com")
pwdent = Entry(width=20)
pwdent.grid(column=1,row=3)

# buttons

generate = Button(text="Generate Password",command=pwdgen)
generate.grid(column=1,row=4)
add = Button(text="Add",command=add)
add.grid(column=2,row=3)
encrypt = Button(text="Encrypt",command=encrypt)
encrypt.grid(column=0,row=0)
decrypt = Button(text="Decrypt",command=decrypt)
decrypt.grid(column=2,row=0)



window.mainloop()