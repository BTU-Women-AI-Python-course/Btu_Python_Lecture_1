bool1 = True
bool2 = False

num1 = 1
num1_float = 1.5

name = input("name: ")
surname = input("surname: ")

print(f"{name}-{surname}")

string1 = "abc"
string1 = string1 + "d"
print(string1)

list1 = ["abc", 1, ["13", 1]]
list1[0] = "abc1"
print(list1)

dict1 = {"key": "value"}
dict1["key"] = "value1"
print(dict1)

tuple1 = (1,2,3)
print(tuple1[0])
# no tuple1[0] = 2
list1.append(tuple1)
print(list1)
tuple2 = tuple(list1)
print(tuple2)

set1 = {"abc", "gh", "abc"}
print(set1) # there is no second abc
set1.add("abc1")
print("abc" in set1)

print(type("str"))
print(type(1))
print(type({"key":"value"}))
print(type(None))