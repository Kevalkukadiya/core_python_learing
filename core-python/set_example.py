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
set_2 = {1,4, 5, 6}

unione_set = set | set_2
print(unione_set)

print("Popped element:", set.pop())

set1 = {1, 2, 3, 4, 5}
set3 = {4, 5, 6, 7, 8}

intersection_set = set1.intersection(set3)

print("Set1:", set1)
print("set3:", set3)
print("Intersection of set1 and set3:", intersection_set)
