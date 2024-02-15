"""
# Lists
names = [
    "Jimmy",
    "Billy",
    "John",
    "Sally",
    "Joe",
    "Johnny"
    ]

popped_name = names.pop(0)
print(popped_name)


popped_name = "Jimbo"

names.insert(0, popped_name)
print(names)


names.insert(len(names), "Sol")
print(names)


numbers = [1, 2, 3, 4, 5]
ex_numbers = [6, 7, "Yes", False, "John"]

numbers.extend(ex_numbers)
print(numbers)


if "Billy" not in names:
    print("Not in list")

name = names[0]
print(names[0][0])


# Same result
for i in names:
    print(i)

for i in range(len(names)): # range(7)
    print(names[i])
    if names[i] == "Joe":
        names[i] = "Mandy"

print(names)

# Dictionaries

my_dictionary = {
                "name":"Terry",
                "age":23,
                "is_funny":False
                } # key : value , key : value

popped = my_dictionary.pop("is_funny")
print(popped)


for key, value in my_dictionary.items(): # i = keys, j = values
    print(f"{key} : {value}")


my_dictionary['is_funny'] = popped
print(my_dictionary)

reference = my_dictionary["age"]
print(reference)

value = my_dictionary.get("none")
print(value)

my_dictionary["is_cool"] = True
print(my_dictionary)

names = ["John Python", "Sol Badguy", "Kazuya Mishima", "Terry Bogard"]
# Change into dictionary : Key = name : value = surname
name_dictionary = {}

for i in names:
    names = i.split(" ")
    print(names)

    name = names[0]
    surname = names[1]
    print(surname)
    name_dictionary[name] = surname
    
print(name_dictionary)


test_list = ["Test", 123]
new_dict_copy = {False: True, 1.234: "This is a float", "The String" : 123, 10: False}

new_dict = {False: True, 1.234: "This is a float", "The String" : 123, 10: False}

new_dict[new_dict_copy[False]] = "Test"
print(new_dict)


list_1 = [1, 2, 3]
list_2 = ["Two", "Three", "One", "Four"]

new_dict = {}

if len(list_1) == len(list_2):
    print("We can make a dict!")

    for num in range(len(list_1)):
        new_dict[list_1[num]] = list_2[num]

print(new_dict)
"""

# Add a new letter at the end of a list with append
"""
new_list = ["a", "b", "c"]
new_letter = "X"
new_list.append(new_letter)
print(new_list)
"""

# Show how to seperate strings and numbers from a list and put them in a new list
"""
mix_list = ["1", 1, "b", 2, "1", 3]
num_list = []
char_list = []

test = "test"

for value in mix_list:
    value_type = f"{type(value)}"

    if value_type == "<class 'str'>":
        char_list.append(value)
    
    elif value_type == "<class 'int'>":
        num_list.append(value)

print(num_list)
print(char_list)

"""
# Print out both values in a dictionary

# arithmatic opperations on a list

nums = [1,2,3,4,5,6,7]

total = 0

for num in nums:
    total += num

print(total)

average = total / len(nums)
print(average)
