# Scripts in Python

from sys import argv # argv is for arguments and sys (system), import is the plan you want to use(aka librariers/modules/features)

script, first, second, third, = argv # unpacks argv or argument, storing 4 variables in argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
 
 # this code only runs on a command line, it would not run compiling it
 # command line input: python3 script.py potatoes onions carrots