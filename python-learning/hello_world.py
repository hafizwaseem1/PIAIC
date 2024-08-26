# # 1
# print("hello world")
# print("waseem")
# #2
# print("Waseem Mughal")
# print("1,2,3")
# #3
# print("Hello\nWorld")
# print("Hello\tWorld")
# #4
# print("Apple","Banana","Cherry", sep=',')
# print(1,2,3 , sep='-' )
# #5
# print("Hello", end=' ')
# print("World")
# print(1 , end="")
# print(2)
# #6
# print("He Said: \"Hello!\"")
# print("This is a backslash:\\")
# #7
# age=20
# print(f"i am {age} Years Old")
# number=5
# print(f"the number is {number}")
# #8
# number1=12345
# for digit in str(number1):
#     print(digit)

# string :str
# integer:int 
# Boolean: bool
# Float: float


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("Type 'stop' to exit.")

        # Take input from the user for the operation
        choice = input("Enter choice (1/2/3/4) or 'stop': ")

        if choice.lower() == 'stop':
            print("Calculator exiting...")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                if result == "Error! Division by zero.":
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid input")

# Run the calculator
calculator()
