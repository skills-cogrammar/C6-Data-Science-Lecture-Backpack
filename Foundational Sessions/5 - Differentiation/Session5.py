import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, sin, cos, exp, log

# Define the symbol for the variable
x = symbols('x')

# 1. Constant Rule: The derivative of a constant is 0
constant = 5
constant_derivative = diff(constant, x)
print(f"Constant Rule: derivative of {constant} is {constant_derivative}")

# 2. Power Rule: The derivative of x^n is n*x^(n-1)
power_function = 16 * x**6
power_rule_derivative = diff(power_function, x)
print(f"Power Rule: derivative of {power_function} is {power_rule_derivative}")

# 3. Constant Multiple Rule: The derivative of a constant times a function is the constant times the derivative of the function
constant_multiple_function = 2*x - 7
constant_multiple_derivative = diff(constant_multiple_function, x)
print(f"Constant Multiple Rule: derivative of {constant_multiple_function} is {constant_multiple_derivative}")

# 4. Sum Rule: The derivative of a sum is the sum of the derivatives
sum_function = x**2 + x**3
sum_rule_derivative = diff(sum_function, x)
print(f"Sum Rule: derivative of {sum_function} is {sum_rule_derivative}")

# 5. Difference Rule: The derivative of a difference is the difference of the derivatives
difference_function = x**3 - x
difference_rule_derivative = diff(difference_function, x)
print(f"Difference Rule: derivative of {difference_function} is {difference_rule_derivative}")

# 6. Product Rule: The derivative of a product of two functions is the first times the derivative of the second plus the second times the derivative of the first
product_function = (x**2) * (x**3)
product_rule_derivative = diff(product_function, x)
print(f"Product Rule: derivative of {product_function} is {product_rule_derivative}")

# 7. Quotient Rule: The derivative of a quotient of two functions is the denominator times the derivative of the numerator minus the numerator times the derivative of the denominator all over the denominator squared
quotient_function = (x**3 + 4*x - 9)/(x + 6)
quotient_rule_derivative = diff(quotient_function, x)
print(f"Quotient Rule: derivative of {quotient_function} is {quotient_rule_derivative}")

# 8. Chain Rule: The derivative of a composite function is the derivative of the outer function evaluated at the inner function times the derivative of the inner function
inner_function = sin(x)
outer_function = inner_function**2
chain_rule_derivative = diff(outer_function, x)
print(f"Chain Rule: derivative of {outer_function} with respect to the inner function {inner_function} is {chain_rule_derivative}")

# Bonus: Exponential and Logarithmic Differentiation
# Exponential Rule: The derivative of e^x is e^x
exponential_function = exp(x)
exponential_derivative = diff(exponential_function, x)
print(f"Exponential Rule: derivative of e^x is {exponential_derivative}")

# Logarithmic Rule: The derivative of log(x) is 1/x
logarithmic_function = log(x)
logarithmic_derivative = diff(logarithmic_function, x)
print(f"Logarithmic Rule: derivative of log(x) is {logarithmic_derivative}")

