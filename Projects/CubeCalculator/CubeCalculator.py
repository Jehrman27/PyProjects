# This program will calculate the surface area of a cube from the value of its edge.

#-------------declarations-------------#

userName = ""
lenEdge = 1
areaCube = 1
total = 1

#-------------function definitions-------------#

# function that welcomes the user
def welcome(name):
    print(F"Welcome to the cube surface area calculator, {name}.")

# function that explains what the program does
def programDesc():
    print(
        "This program will calculate the surface area of a cube from the "
        "entered value of its edge."
        )

# function that prints the calculated surface area of a face of a cube
def surfaceFace(x):
    x = int(x)
    face = x * x
    print(F"The surface area of one face of the cube is {face} units.")

# function that returns the calculated surface area of a cube
def surfaceCube(x):
    x = int(x)
    area = 6 * x ** 2
    return area

#-------------main line logic-------------#

# get user's name
userName = input("Please enter your name: ")

# welcome user (objectives didn't explicitly say to call this fuction, but included just in case.)
#elcome(userName)

# describe purpose of the program
programDesc()

# get length of edge from user
lenEdge = input("Please enter the length of the edge: ")

# calculate a face of the cube (objectives didn't explicitly say to call this fuction,
#   but included just in case.)
#surfaceFace(lenEdge)

# calculate and print surface area of cube
total = surfaceCube(lenEdge)
print(F"The surface area of the whole cube is {total} units.")



