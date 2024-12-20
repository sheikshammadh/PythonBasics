def calculate(a, b):
    """This function calculates the sum, difference, product, division, and modulus of two numbers."""
    
    total = a + b
    diff = a - b
    prod = a * b
    div = a / b if b != 0 else 'Division by zero not allowed'
    mod = a % b if b != 0 else 'Modulus by zero not allowed'
    
    return total, diff, prod, div, mod

# Taking input from the user
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))

# Calling the function and printing the results
total, diff, prod, div, mod = calculate(a, b)
print(f"Sum: {total}, Difference: {diff}, Product: {prod}, Division: {div}, Modulus: {mod}")
