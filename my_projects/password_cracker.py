# Python code snippet to guess user password comprised of all letters and digits

import string 
import os
from random import *


u_pwd = input("Enter your password: ")
pwd = list(string.digits + string.ascii_letters)

pw = ""
while (pw != u_pwd):
    pw = ""
    for char in range(len(u_pwd)):
        guess_pwd = pwd[randint(0, len(pwd) - 1)]
        pw = str(guess_pwd)+str(pw)
        print(pw)
        print("Cracking password...Please wait!")
        os.system("cls")
    
print("Your password is : ", pw)