def print_two(*args): #this is a function, we use def to define a function
    arg1, arg2 = args #creates 2 arguments
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_two_again(arg1, arg2, arg3):

    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")

# this takes one argument
def print_one(arg1):

    print(f"arg1: {arg1}")

# this takes no arguments
def print_none():

    print("I got nothin'.")


print_two("Zed","Shaw") # Zed and Shaw will be saved in one of the 2 variables
print_two_again("Zed","Shaw", "Varsha")
print_one("First!")
print_none()