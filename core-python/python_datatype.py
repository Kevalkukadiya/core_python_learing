# """
# List :- List is Ordered Collection, Muteable that means you can add , update and delete
#         after creation
# """
# my_list = [1, 2, 3, "Hello", 4, 5, 6]
# print("List ", my_list)

# my_list.append(4)
# print("Add 4 in List ", my_list)

# my_list.remove("Hello")
# print("Remove Hello from List ", my_list)

# my_list[2] = 5
# print(my_list)

# my_list = [x for x in my_list if x != 5]
# print(my_list)

# """
# Dictionaries :- dictionary is an unordered collection of key-value pairs.
#                 Dictionaries are defined using curly braces {}. Each key in a dictionary must be unique.
# """

# my_dict = {"name": "Kukadiya Keval", "age": 20, "city": "Ahmedabad"}
# print(my_dict)

# my_dict["profession"] = "Python Devloper"
# print(my_dict)

# my_dict = {
#     "name": ["Kukadiya Keval", "Alice"],
#     "age": [20, 21],
#     "city": "Ahmedabad",
# }
# print(my_dict)

# my_dict.pop("age")
# print(my_dict)

# print(my_dict.get("city"))


"""
Set :- unordered collection of unique elements. The primary characteristics of sets are that 
        they don't allow duplicate values, and the order of elements is undefined. 
        Sets are mutable, meaning you can add and remove elements from them.
"""
set = {1, 2, 3, 4, 6}
print("set", set)

set.add(5)
print("Add Elemnt Set", set)

set.remove(6)
print("Remove Element Set", set)

set = {1, 2, 3, "Hello"}
set_2 = {4, 5, 6}

unione_set = set | set_2
print(unione_set)
