# -*- coding: utf-8 -*-
"""Day 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QB4Doo9GV5jtEIAco0dXQa5GlRjwPTp7
"""

#Assignment 2 :Remove all occurences in list
li=[2,3,4,5,6,2]
li.remove(2)
print(li)
li.remove(2)
print(li)

# Assignment 3: Chech whether a string is pangram
import random as r
import string
pangram=''
characters=string.ascii_letters
print(characters)
pangram=pangram+r.choice(characters)
print("Yes:",pangram)

#OTP Generator project
import random  as r
import string
length =6
otp=''
characters=string.ascii_letters+string.digits
print(characters)
for i in range (length): 
  otp=otp+r.choice(characters)
print("OTP:",otp)