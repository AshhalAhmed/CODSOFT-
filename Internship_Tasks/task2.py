                                            # task2
# CALCULATOR
# Design a simple calculator with basic arithmetic operations. Prompt the user to input two numbers and an operation choice. Perform the calculation and display the result.
print("Welcome to python calculator")
print("Select an operation")
while True:
    print(f"1)Addition")
    print(f"2)Subtraction")
    print(f"3)Multiplication")
    print(f"4)Division")
    print(f"5)Exit")
    user_input=input("Enter choice (1,2,3,4,5): ")
    if user_input == '5':
        print("Exiting the calculator. Goodbye!")
        break
    if user_input=="1":
        first=int(input("Enter the First number: "))
        second=int(input("Enter the Second number: "))
        Result=first+second
        print(f"Result:{first}+{second} = {Result}")
    elif user_input=="2":
        first=int(input("Enter the First number: "))
        second=int(input("Enter the Second number: "))
        Result=first-second
        print(f"Result: {first} - {second} = {Result}")
    elif user_input=="3":
        first=int(input("Enter the First number: "))
        second=int(input("Enter the Second number: "))
        Result=first*second
        print(f"Result: {first} * {second} = {Result}")
    elif user_input=="4":
        first=int(input("Enter the First number: "))
        second=int(input("Enter the Second number: "))
        Result=first/second
        print(f"Result: {first} / {second} = {Result:.2f}")   
    else:print("Try to Enter talid choice")
