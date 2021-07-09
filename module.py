# 2) Create a Module in VS Code and Import It into jupyter notebook
# Module should have the following capabilities:

# 1) Has a function to calculate the square footage of a house
# Reminder of Formula: Length X Width == Area

# 2) Has a function to calculate the circumference of a circle

# Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage

length = 25
width = 40

def area(length, width):
    square_feet = (length * width)
    print(f'Your house is {square_feet} square feet.')

print(area(25,40))


def circle(r):
    cir = (3.14*r*2)
    return cir

circle(6)