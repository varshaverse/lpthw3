 # More Formatting

formatter = "{} {} {} {}" # this creates a list
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter)) # this prints braces 9 times
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"

))
print("\n")
list = "{} {} {} "
print(list.format("List: " 'milk,', 'onions,', 'banana')) # prints a shopping list
