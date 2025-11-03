# Ask user for 2 numbers and an operation

num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your second number:"))
operation = input("Enter Operation (+, - , *, /):")
result = None


# Perform the operation based on user input
if operation == "+":
    result = num1 + num2
elif operation =="-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2 
    if num2 != 0:
        result = num1/num2
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("invalid operation")

# Show the result only if it’s valid
if result is not None:
    print("The result is:", result)