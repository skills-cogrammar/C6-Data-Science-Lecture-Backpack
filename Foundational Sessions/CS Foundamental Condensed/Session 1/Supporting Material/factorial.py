#factorial

# 6! = 6 * (n- 1)!

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(6))