
# Labda function examples
lambda : print("Hello World")

greeting = lambda : print("Why hello there")
greeting()


# calculates the value of the variable with 2 being added
add_two = lambda x : x + 2
print(add_two(5))

# example of a regular function that also adds two for comparison
def add_2(x):
    return x + 2

print(add_2(6))

# calculates the value of the variable cubed
cube = lambda y : y ** 3
print(cube(3))

# example of a lambda functions that does not require a variable VS one that does
old_greeting = lambda : print("Hello World")
greeting = lambda x : print(f"Welcome back {x}")

# example lambda function called with no variable being passed
old_greeting()
# example lambda function called with a variable being passed
greeting("Tom")

# lambda function being called but not saved to a variable
get_username = lambda : input("Please enter your username: ")
print(get_username())

# lambda function being saved to a variable to print out the returned result
new_user = get_username()
print(f"This is the new user {new_user}")

# lambda function with multiple values being passed to it
show_user = lambda user, user2, user3 : print(f"Welcome:\n{user}\n{user2}\n{user3}")
show_user("Mr X", "Mr Y", "Mr Z" )



# regular recursive function
def factorial(n):
    print(n)
    if n == 1:
        return 1
    
    else:
        return n * factorial(n - 1)

print(factorial(5))

# creates a recursive functions that loops endlessly
def drop_one(sample_string, index_range=0):
    if index_range == 0:
        index_range = len(sample_string)

    print(sample_string[:index_range])
    if index_range == - len(sample_string):
        return
    
    else:
        return drop_one(sample_string, index_range-1)

drop_one("Hello")
