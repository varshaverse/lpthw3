#Reading files in Scripts
from sys import argv # sys is a package and argv is just a feature of that package

script, filename = argv


txt = open(filename) # opens the file

print(f"Here's your file {filename}:")
print(txt.read()) # reads the file, read is a function

print("Type the filename again:")
file_again = input("> ")


txt_again = open(file_again)


print(txt_again.read())

# run this program doing python3 [python file] [script file] on comman prompt