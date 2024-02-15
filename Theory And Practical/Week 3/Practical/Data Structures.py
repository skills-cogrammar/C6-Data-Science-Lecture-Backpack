names = [
    "Jimmy",
    "Billy",
    "John",
    "Sally",
    "Joe",
    "Johnny"
    ]

# popped_name = names.pop(0)
# print(popped_name)
# print(names)

# popped_name = "Jimbo"

# names.insert(2, popped_name)
# print(names)


# names.insert(0, "Sol")
# print(names)


# numbers = [1, 2, 3, 4, 5]
# ex_numbers = [6, 7, "Yes", False, "John"]

# numbers.extend(ex_numbers)

# print(numbers)

# names = ["Picollo", "Vegeta", "Goku"]
# if "Vegeta" in names:
#     print("Element exists in the list")
# else:
#     print("Element does not exist in the list")


# name = names[0]
# print(name[1])

# names=["Bon Jovi", "Freddie Mercury", "Pink Floyd"]

# for i in names:  #foreach loop in python
#     print(i)

# for i in range(len(names)): # for loop in python
#     print(names[i])





# my_dictionary = {
#                 "name":"Terry",
#                 "age":23,
#                 "is_funny":False
#                 }


# popped = my_dictionary.pop("name")
# print(popped)
# print(my_dictionary)

my_dictionary = {
                "name":"Goku",
                "age":23,
                "power_level":9000
                }

print(my_dictionary.items())
for key, value in my_dictionary.items():
    print(f"{key} : {value}")

print(my_dictionary.values())
for value in my_dictionary.values():
    print(value)

print(my_dictionary.keys())
for key in my_dictionary.keys():
    print(key)


my_dictionary = {
                "name":"Vegeta",
                "age":23,
                "power_level":9000
                }

my_dictionary['power_level'] = 10
print(my_dictionary)

reference = my_dictionary["age"]
print(reference)

value = my_dictionary.get("name")
print(value)


# my_dictionary["is_cool"] = True
# #print(my_dictionary)

# names = ["John Python", "Sol Badguy", "Kazuya Mishima", "Terry Bogard"]
# # Change into dictionary : Key = name : value = surname
# name_dictionary = {}

# for i in names:
#     names = i.split(" ")
#     # print(names)

#     name = names[0]
#     surname = names[1]
#     # print(surname)
#     name_dictionary[name] = surname
    
# print(name_dictionary)
