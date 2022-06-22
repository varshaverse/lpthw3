# A Text Editor

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.") # opens the file
print("If you don't want that, hit CTRL-C (^C).") # asks for input 
print("If you do want that, hit RETURN.")

input('?')
print("Opening the file...")
target = open(filename, 'w') # opens the file, w stands for  writemode for writing

print("Truncating the file. Goodbye")
target.truncate() # truncates means erase the contents of the file
print("Now I'm going to ask you for three lines.") #  asks for input again so data can be written in the same file
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.") # all lines from input are transferred to the existing document mentioned
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
 
print("And finally, we close it.")
target.close() #closes the file

#On the command line you see:
# python3 tedit.py sread.txt

# it would not run if you do not do it properly

