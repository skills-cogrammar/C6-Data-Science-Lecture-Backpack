n=int(input("Enter the input number:"))
if n % 2 != 0:  #odd
    print("Weird")
else:           #even
    if n>=2 and n<=5:
        print("Not Weird")
    
    if n>=6 and n<=20:
        print("Weird")

    if n > 20:
        print("Not Weird")