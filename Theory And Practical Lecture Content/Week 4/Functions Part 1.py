"""
import random as rd

cpu_choice = rd.randint(1,3)
print(cpu_choice)

user_choice = int(input("Enter 1 for rock, 2 for paper, 3 for scissors : "))

# 1 = rock
# 2 = paper
# 3 = scissors
if cpu_choice == 1 and user_choice == 2:

    print("You win!")
    print("Paper beats rock!")

elif cpu_choice == user_choice:

    print("Its a tie!")

# The other checks
"""
'''
def addition(x = 5, y = 0):
    """
    Adds two numbers together
    """
    return x + y

num_1 = int(input("Please enter a number : "))
num_2 = int(input("Please enter a number : "))

total = addition(y = num_2)
print(total)
'''
'''
def addition():
    """
    Adds two numbers together
    """
    x = int(input("Please enter a number : "))
    y = int(input("Please enter a number : "))

    return x + y

total = addition()
print(total)
'''

"""
def is_even(num):

    while True:
        if num % 2 == 0:
            print("Your number is even")
            return
        else:
            print("Your number is NOT even")
            return

test = is_even(num=3)
print(num)
"""
'''
def get_int(display_string = "Please enter a number: "):
    """
    Continues to ask the user for an int, until a valid int is entered.
    """

    while True:
        user_input = input(display_string)

        try:
            user_input = int(user_input)
            return user_input
        
        except:
            print("Please only enter a number.")

total = 0
while True:
    user_choice = get_int("Please enter an int -> ")

    if user_choice == -1:
        break
    
    total += user_choice

print(f"This is the Total: {total}")
'''
