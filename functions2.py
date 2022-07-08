# More Functions

def cheese_and_crackers(cheese_count, boxes_of_crackers): # this is a function, def is define

    print(f"You have {cheese_count} cheeses!") # subsitutes 20 for cheese count
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n") # prints a new line


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) # first call of function


print("OR, we can use variables from our script:")
amount_of_cheese = 10 # new variables with new value
amount_of_crackers = 50


cheese_and_crackers(amount_of_cheese, amount_of_crackers) # 2nd calling function


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6) #uses 30 and 11 for chees count and box of crackers

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # last calling function
