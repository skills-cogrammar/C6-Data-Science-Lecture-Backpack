'''
Noticed in the lecture a lot of you asked how to keep asking the user for input without repeating
the whole program altogether. So basically its just a matter of seperating the inputs into two separate
while loops and assigning None to both the variables so to keep asking for the input while the variable
is None. None is a reserved python keyword to denote that a variable has been assigned a null value.
'''
percentage = None
price = None
while percentage is None:
    try:
        percentage = float(input("Enter your percentage:"))
        if percentage < 0 or percentage > 100:
            raise Exception("Percentage should be between 0 and 100.")

        print("Your percentage is " + str(percentage))
    except ValueError:
        print("Please ensure your input is a number.")
        percentage = None

    except Exception as e:
        print(e)
        percentage=None
while price is None:
    try:
        price = float(input("Enter your price:"))
        if price > 1000:
            raise Exception("Price should be below 1000.")
    
    except ValueError:
        print("Please ensure your input is a number.")
        price=None

    except Exception as e:
        print(e)
        price=None

print(price * percentage)