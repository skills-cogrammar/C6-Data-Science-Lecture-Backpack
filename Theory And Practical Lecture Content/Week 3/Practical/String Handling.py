name = "John"
surname = "Python"
curly_bracket = "{}"

print("My name is {} {}, and I am a thorough {} enjoyer \
      ".format(name, surname, "Basketball"))

print("My name is {0} {1}, and I am a thorough {2} enjoyer {{}}".format(name, surname, "Basketball"))

x = "twenty four"
y = 39
z = 13
print("""Your order of : burger, which costs ${}
Your order of : pizza, which costs ${:.2f}
Your order of : pepsi, whcih costs ${:.2f}""".format(x, y, z))
print("a / b = {:.2f}".format(10 / 3))
print("a / b = {:+.2f}".format(10 / 3))
print("a / b = {:.0f}".format(10 / 3))
print("{:0>6d}".format(1000)) # Left padding
print("{:0>6.2f}".format(10 / 3)) # Left padding
print("{:x<6d}".format(100)) # Right padding
print("{:.2%}".format(0.45)) # Percentage format
print("{:,}".format(1000000000000000)) # Commas for large numbers 
print("{:.2e}".format(1000000000000000)) # Exponential formatting
print("{:>10d}".format(1000)) # Right aligned
print("{:<10d}".format(100)) # Left aligned
print("{:x^10d}".format(100)) # Centre aligned



print(f"""Your order of : burger, which costs ${name}
Your order of : pizza, which costs ${surname}
Your order of : pepsi, which costs ${z:.2f}""")

# program that counts how many instances of a character there are in a string

count = 0
sentence = input("Please enter your string : ").lower()
print(sentence)

while True:
    
    character = input("Please enter the character you would like to count : ").lower()

    if len(character) > 1:
        print("You have entered more than one character, please try again ")

    
    elif not character.isalpha():
        print("You have entered a number or symbol. please try again")


    else:
        break

for jam in range(len(sentence)):

    print(f"iteration: {jam} character : {sentence[jam]}")
    if character == sentence[jam]:
        count = count + 1

print(f"The character : {character} appeared {count} times")