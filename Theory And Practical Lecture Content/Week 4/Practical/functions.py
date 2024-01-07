def multiply(x, y):
    print(x * y)

def multiply2(a=2,b=2):
    print(a)
    print(b)
    return a * b

num1=int(input("Input num 1:"))
num2=int(input("Input num 2:"))
print(multiply2(num1, num2))