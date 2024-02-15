# A program that asks the user for a password and returns the strength of a password
import re

def evaluate_password_strength(password):
    #Return the strength of the password (int)
    length_criteria = len(password) >= 8
    uppercase_criteria = False
    lowercase_criteria = False
    digits_criteria = False
    special_characters_criteria = False

    for c in password:
        if c.isupper():
            uppercase_criteria=True
            break

    for c in password:
        if c.islower():
            lowercase_criteria=True
            break

    for c in password:
        if c.isnumeric():
            digits_criteria=True
            break

    special_characters_criteria = bool(
        re.search(r"[!@#$%^&*(),.?\":{}|<>_/]", password))

    strength = 0

    if length_criteria:
        strength+=1
    
    if uppercase_criteria:
        strength+=1

    if lowercase_criteria:
        strength+=1

    if digits_criteria:
        strength+=1

    if special_characters_criteria:
        strength+=1

    return strength


password=input("Enter your password:")
password_strength = evaluate_password_strength(password)
print(f"Password strength is {password_strength}")