# Required Arguments
def student(name, age):
    print("Required Arguments:")
    print("Name:", name)
    print("Age:", age)
    print()


# Keyword Arguments
def employee(name, salary):
    print("Keyword Arguments:")
    print("Name:", name)
    print("Salary:", salary)
    print()


# Default Arguments
def greet(name, message="Welcome!"):
    print("Default Arguments:")
    print(message, name)
    print()


# Variable-Length Arguments
def marks(*scores):
    print("Variable-Length Arguments:")
    print("Marks:", scores)
    print("Total:", sum(scores))
    print()


# Function Calls
student("Rahul", 20)                  # Required arguments

employee(salary=50000, name="Anita")  # Keyword arguments

greet("Priya")                        # Uses default value
greet("Karan", "Good Morning!")       # Custom value

marks(85, 90, 78, 88, 95)             # Variable-length arguments