#Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

name=input("Please type your name: ")

r=name.split(" ")
first=r[0]
last=r[1]

print("Your inversed name would be:",last,first)