import string
from string import *
import random
import os

def password_gen(length):
    chars = string.ascii_lowercase+ string.ascii_uppercase +string.digits +string.punctuation
    
    while True:

     password ="".join(random.choice(chars) for _ in range(length))
     lower = sum(1 for char in password if char in ascii_lowercase)
     upper = sum(1 for char in password if char in ascii_uppercase)
     digit = sum(1 for char in password if char in digits)
     punc = sum(1 for char in password if char in punctuation)

     if lower>1 and upper>1 and digit>1 and punc>1:
        return password

#override when length is given default = 8

def gen_passwords(no_of_passwords,length):
   passwords= set()
   for _ in range(no_of_passwords):
        password = password_gen(length)
        passwords.add(password)

   return passwords



if __name__ == "__main__":
    os.system('cls')

    while True:

        os.system('cls')
        number = int(input("HOW MANY PASSWORDS WOULD YOU LIKE TO GENERATE?\n"))
        length = int(input("length of the password"))
        input("\n password lenght::")
        passwords= gen_passwords(number,length)
        print(f"\n{number} passwords generated succesfuly\n")
        for pwd in passwords:
          print(pwd)



