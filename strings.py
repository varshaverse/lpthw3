#Strings and formatting

my_name = 'Zed A. Shaw' #stores string Zed in the variable my_name
my_age = 35 
my_height = 74 # these are valid variable names
my_weight = 180 
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown' # single quotes or double quotes can be used when writing strings
my_ethnicity = 'Indian'


total = my_age + my_height + my_weight # calculates total values
print("\n")
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.") # uses f for formatting the string when using multiple variables

print(f"Let's talk about {my_name}.") #f is a function in python
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")
print(f"My ethnicty is {my_ethnicity}.")

print("\n")
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious)) #.format another type of formatting that is used in loops and other situations


name = False
name_evaluation = "Isn't your name Bob? {}"
print(name_evaluation.format(name))

