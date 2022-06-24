from sys import argv
from os.path import exists # reserved keyword exists is to see if the file exists


script, from_file, to_file = argv #from file and to file are 2 different files that should be on your pc


print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file) #opens file 
indata = in_file.read()  # reads the original file


print(f"The input file is {len(indata)} bytes long") #len counts the length of the content in the original file

print(f"Does the output file exist? {exists(to_file)}") # returns true or false if the ouput file exists
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w') #opens file for writing and copies content from original file to the empty file
out_file.write(indata) #copies data


print("Alright, all done.")

out_file.close()
in_file.close()
#closes both files