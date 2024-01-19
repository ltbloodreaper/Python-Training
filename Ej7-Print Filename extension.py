# Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java


filename = input("Please insert the name of a file with extension: ")

print(filename[filename.find(".")+1:])
