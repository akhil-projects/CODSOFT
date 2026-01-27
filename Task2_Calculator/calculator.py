# Task 2:  Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

print("Welcome to the Calculator!")
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtract (-)")            
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Enter your choice (1/2/3/4): ")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()

if choice == '1':
    result = add(num1, num2)
    operation = '+'
elif choice == '2':
    result = subtract(num1, num2)
    operation = '-'
elif choice == '3':
    result = multiply(num1, num2)
    operation = '*'
elif choice == '4':
    result = divide(num1, num2)
    operation = '/'
else:
    print("Invalid choice. Please select from 1 to 4.")
    exit()


print(f"\nResult: {num1} {operation} {num2} = {result}")