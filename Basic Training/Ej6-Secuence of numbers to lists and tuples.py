# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates
# a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

import re

numlist=[]

sec=input("Please insert a sequence of numbers separated by commas:")
# Check if your string matches your pattern
if re.match(r'^(\s*\d+\s*\,)*(\s*\d+\s*)$', sec):
    # Split the string from comma 
    arr = sec.split(",")
    
    # For each element in arr, use int() function
    numlist = list(map(int, arr))
    print(numlist)
    print(tuple(numlist))
# Otherwise ask user to input proper string
else:
    print("Please enter a comma between the numbers")


#My previous answer:
# com = 0
# num = 1
# numlist=[]
# aux=0
# for x in sec:
#     if x == "," or x==" ":
#         pass
#     else:
#         try:
#             numlist.append(int(x))
#         except:
#             aux=1

# if aux==1:
#     print("Please just insert numbers and commas")
# else:

#     if x == ",":
#         com+=1
#     elif x == " ":
#         pass
#     else:
#         num+=1

#     if (num-3) < com <= num:

#         print(numlist)
#         print(tuple(numlist))
#     else:
#         print("Please enter a comma between the numbers")