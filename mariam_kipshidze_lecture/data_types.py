# Integer
integer_var = 42
print("Integer:", integer_var, "Type:", type(integer_var))

# Float
float_var = 3.14
print("Float:", float_var, "Type:", type(float_var))

# String
string_var = "Hello, Python!"
print("String:", string_var, "Type:", type(string_var))

# Boolean
boolean_var = True
print("Boolean:", boolean_var, "Type:", type(boolean_var))

# List
list_var = [1, 2, 3, "four", "five"]
print("List:", list_var, "Type:", type(list_var))

# Accessing list elements
print("First element of the list:", list_var[0])
print("Last element of the list:", list_var[-1])

# Tuple
tuple_var = (1, 2, 3, "four", "five")
print("Tuple:", tuple_var, "Type:", type(tuple_var))

# Accessing tuple elements
print("First element of the tuple:", tuple_var[0])
print("Last element of the tuple:", tuple_var[-1])

# Dictionary
dict_var = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("Dictionary:", dict_var, "Type:", type(dict_var))

# Accessing dictionary values
print("Name:", dict_var["name"])
print("Age:", dict_var["age"])

# Set
set_var = {1, 2, 3, 4, 5}
print("Set:", set_var, "Type:", type(set_var))

# Adding and removing elements in a set
set_var.add(6)
print("Set after adding 6:", set_var)
set_var.remove(1)
print("Set after removing 1:", set_var)

# Demonstrating type conversion
num_str = "123"
num_int = int(num_str)
print("Converted to integer:", num_int, "Type:", type(num_int))

# Floating point division
div_result = 10 / 3
print("Division Result:", div_result, "Type:", type(div_result))

# String formatting
name = "Bob"
greeting = f"Hello, {name}!"
print("Formatted String:", greeting)
