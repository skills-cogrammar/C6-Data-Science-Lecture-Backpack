n=int(input("Enter your number:"))
if n % 2 != 0:
    print("Weird")
else:
    if n >= 2 and n <= 5:
        print("Not weird")
    
    if n >= 6 and n <= 20:
        print("Weird")
    
    if n > 20:
        print("Not weird")