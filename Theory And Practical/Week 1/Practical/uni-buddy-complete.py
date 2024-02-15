
name=input("What is your name? ")
age=int(input("What is your age? "))
fav_col=input("What is your favourite colour? ")

print("\n\nHey " + name + ", good to see you. My name is UniBuddy, your trusty university chatbot.")

if age > 30:
    print("Ah I see you are in your 30s now, might be a good time for a reunion with your school buddies?")
elif age >= 20 and age < 30:
    print("Ah, you got time")
elif age < 20:
    print("What are you doing here? Go out! Have fun!")
else:
    print("Do whatever you like.")

if fav_col == "blue":
    print("Join the blue baracuda dancing club.")
elif fav_col=="red":
    print("Join the pokemon red ribbon army.") 
