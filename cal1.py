print("Welcome to the world of math\t\n1.Add\n2.Subtract\n3.Divide\n4.Mulitply")
num1 = float(input("Enter first number:"))
operator = input("Enter operator:")
num2 = float(input("Enter second number:"))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1/num2)
elif operator == "*":
    print(num1*num2)
else:
    print("Invalid operator")    
