print("1 - ADD")
print("2 - SUBTRACT")
print("3 - MULTIPLY")
print("4 - DIVIDE")
opt = int(input("Enter the number for operation you need: "))

if opt in [1, 2, 3, 4]:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if opt == 1:
        result = num1 + num2
    elif opt == 2:
        result = num1 - num2
    elif opt == 3:
        result = num1 * num2
    else:
        
        if num2 != 0:
            result = num1 // num2
        else:
            result = "Undefined (division by zero)"
else:
    print("Invalid Input")
    result = None

if result is not None:
    print("The Result Of Operation Is :", result)
