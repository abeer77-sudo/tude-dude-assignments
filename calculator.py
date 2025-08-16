a=int(input("Enter first no.:"))
ch=input("Enter operation (+, -, *, /): ")
b=int(input("Enter second no.:"))
match ch:
    case '+':
        print(f"Addition = {a + b}")
    case '-':
        print(f"Subtraction = {a - b}")
    case '*':
        print(f"Multiplication = {a * b}")  
    case '/':
        if b != 0:
            print(f"Division = {a / b}")
        else:
            print("Error: Division by zero is not allowed.")