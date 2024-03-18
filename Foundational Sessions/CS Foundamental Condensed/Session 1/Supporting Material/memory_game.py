import sys

list_numbers = [1,2,3,4,5,6]
list_fruits = ["orange", "strawberry", "mango"]
list_bool = [True, False]

# for item in list_fruits:
#     print(f"id of item {item} is {hex(id(item))}. Its size is {sys.getsizeof(item)}")

# for item in list_numbers:
#     print(f"id of item {item} is {hex(id(item))}. Its size is {sys.getsizeof(item)}")

for item in list_bool:
    print(f"id of item {item} is {id(item)}. Its size is {sys.getsizeof(item)}")