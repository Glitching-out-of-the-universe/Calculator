#  adds two numbers
def add(x, y):
    return x + y


#subtracts two numbers
def subtract(x, y):
    return x - y


# multiplies two numbers
def multiply(x, y):
    return x * y


#this divides two numbers
def divide(x, y):
    return x / y

# Select operation
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
#if operation chosen is correct then
while True:

    choice = input("Enter your choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    # if operation is not correct
    else:
        print("Invalid")
