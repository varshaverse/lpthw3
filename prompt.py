# Prompts and Passing

from sys import argv

script, name = argv #data is stored for variable name
prompt = '-' # prompt is a reserved keyword  

print(f"Hi {name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {name}?")
like = input(prompt)

print(f"Where do you live {name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {like} about liking me.
You live in {lives}.
And you have a {computer} computer.
""")

#on the command line, python3, [filename], [variablename]