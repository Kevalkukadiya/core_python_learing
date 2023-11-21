"""
List :- List is Ordered Collection, Muteable that means you can add , update and delete
        after creation
"""
my_list = [1, 2, 3, "Hello", 4, 5, 6]
print("List ", my_list)

my_list.append(4)
print("Add 4 in List ", my_list)

my_list.remove("Hello")
print("Remove Hello from List ", my_list)

my_lists = [1, 2, 3]
for list in my_lists:
    print(list)

print("Hello" in my_list)  # False


my_list[2] = 5
print(my_list)

my_list = [x for x in my_list if x != 5]
print(my_list)

# Creating a list of squares of numbers from 0 to 9 using a for loop
one_ten_loop = []
one_ten_loops = []

for num in range(10):
    one_ten_loop.append(num)
    one_ten_loops.append(num * 2)

print("Print 10 Number for loop:", one_ten_loop)
print("Multi using  for loop:", one_ten_loops)


squares_using_comprehension = [num ** 2 for num in range(10)]
print("Using list comprehension:", squares_using_comprehension)

