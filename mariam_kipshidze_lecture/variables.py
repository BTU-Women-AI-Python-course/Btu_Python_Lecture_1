# Integer
age = 30
print("Age:", age, "Type:", type(age))

# Float
height = 5.9
print("Height:", height, "Type:", type(height))

# String
message = "Hello, World!"
print("Message:", message, "Type:", type(message))

# Boolean
is_student = True
print("Is student:", is_student, "Type:", type(is_student))

# Assigning values to variables
x = 5
y = 10
name = "Alice"

print("x =", x)
print("y =", y)
print("name =", name)

# Reassigning values
x = 20
print("New value of x =", x)


# Assign multiple variables at once
a, b, c = 1, 2, "Three"
print("a =", a)
print("b =", b)
print("c =", c)

# Swapping variables
a, b = b, a
print("Swapped a =", a)
print("Swapped b =", b)


# Arithmetic operations
num1 = 15
num2 = 4

sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
remainder = num1 % num2

print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
print("Remainder:", remainder)

# Concatenating strings
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full Name:", full_name)


# Global variable
global_var = "I am a global variable"


def my_function():
    # Local variable
    local_var = "I am a local variable"
    print(local_var)
    print(global_var)


my_function()

# Uncommenting the following line will raise an error because local_var is not accessible outside the function
# print(local_var)

print(global_var)

# Using constants (conventionally written in uppercase)
PI = 3.14159
GRAVITY = 9.81

radius = 5
circle_area = PI * (radius ** 2)

print("Circle Area:", circle_area)

# Correct variable names
my_variable = 10
_myVariable = 20
variable123 = 30

print("my_variable:", my_variable)
print("_myVariable:", _myVariable)
print("variable123:", variable123)

# Incorrect variable names (will cause syntax errors)
# 123variable = 40  # Cannot start with a number
# my-variable = 50  # Cannot contain hyphens
# def = 60          # Cannot use reserved keywords
