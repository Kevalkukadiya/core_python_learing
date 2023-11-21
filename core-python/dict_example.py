"""
Dictionaries :- dictionary is an unordered collection of key-value pairs.
                Dictionaries are defined using curly braces {}. Each key in a dictionary must be unique.
"""

my_dict = {"name": "Kukadiya Keval", "age": 20, "city": "Ahmedabad"}
print(my_dict)

my_dict["profession"] = "Python Devloper"
print("Add new Key-Value ", my_dict)

print("Get City", my_dict.get("city"))

print("Copy of Dict :", my_dict.copy())

print("Return Key-Value : ", my_dict.get("age", None))

print("dictionary's keys :", my_dict.keys())

print("dictionary's values :", my_dict.values())

# print("Remove Age", my_dict.pop("age"))

if "Alice" in my_dict.values():
    print("Yes")
else:
    print("No")

my_dict = {
    "name": ["Kukadiya Keval", "Alice"],
    "age": [20, 21],
    "city": "Ahmedabad",
}
print(my_dict)

print("Removes all items :", my_dict.clear())

# Creating a dictionary of 1 to 10
range_dict = {}

for num in range(1, 10):
    range_dict[num] = num

print(range_dict)

for num in range(1, 10):
    range_dict[num] = num * 2

print(range_dict)

