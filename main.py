import random
import pyperclip
from tkinter import *

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', '{', '}', '[', ']', '|', '\\', ':',
           ';', '<', ',', '>', '.', '?', '/']

window = Tk()
window.title("Strong Password Generator")
window.config(padx=50, pady=50)

new_password = []


def password_generator():
    global new_password
    password = []
    for each_letter in range(int(number_of_letters.get())):
        password.append(random.choice(letters))
    for each_symbol in range(int(number_of_symbols.get())):
        password.append(random.choice(symbols))
    for each_number in range(int(number_of_numbers.get())):
        password.append(random.choice(numbers))
    random.shuffle(password)
    new_password = ''.join(password)
    password_generated.config(text=new_password)


def copy():
    pyperclip.copy(new_password)


password_generated = Label(text="password")
password_generated.grid(column=2, row=3)

letters_label = Label(text="# of Letters :")
numbers_label = Label(text="# of Numbers :")
symbols_label = Label(text="# of Symbols :")

password_label = Label(text="Password :")
password_label.grid(column=1, row=3)

button = Button(text="Generate", width=13, command=password_generator)
button.grid(column=1, row=4)

copy_button = Button(text="Copy", width=13, command=copy)
copy_button.grid(column=2, row=4)

# Using Scale
# letters_label.grid(column=1, row=0)
# numbers_label.grid(column=2, row=0)
# symbols_label.grid(column=3, row=0)
# number_of_letters = Scale(from_=0, to=10, width=20)
# number_of_numbers = Scale(from_=0, to=10, width=20)
# number_of_symbols = Scale(from_=0, to=10, width=20)
# number_of_letters.grid(column=1, row=2)
# number_of_numbers.grid(column=2, row=2)
# number_of_symbols.grid(column=3, row=2)

# Using Spinbox
letters_label.grid(column=1, row=0)
numbers_label.grid(column=1, row=1)
symbols_label.grid(column=1, row=2)
number_of_letters = Spinbox(from_=0, to=10, width=5)
number_of_numbers = Spinbox(from_=0, to=10, width=5)
number_of_symbols = Spinbox(from_=0, to=10, width=5)
number_of_letters.grid(column=2, row=0)
number_of_numbers.grid(column=2, row=1)
number_of_symbols.grid(column=2, row=2)

window.mainloop()
