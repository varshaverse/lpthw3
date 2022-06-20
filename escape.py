#Escape Sequences

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" # /n prints a new line

print("Here are the days: ", days)
print("Here are the months: ", months)

print(""" 
There's something going on here. 
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
# use triple quotes for multiple lines

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line." # goes to new line then prints, on a line
backslash_cat = "I'm \\ a \\ cat." # 2 backlashes is one backslash

fat_cat = """
I'll do a list:
\t* Cat food 
\t* Fishies
\t* Catnip\n\t* Grass
"""
# /t indents the line

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)