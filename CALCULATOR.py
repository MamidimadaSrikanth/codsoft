# Make a simple caluculator with 4 basic operation
#this operation specify the addition
def add(x, y):
    return x + y
# this operation specify the subtraction
def sub(x, y):
    return x - y
# this operation specify the multiplication
def mul(x, y):
    return x * y
# this operation specify the division
def div(x, y):
    return x / y
print("select the operation")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
while True:
    #take input from user
    choice = input("enter your choice(1/2/3/4): ")
    #check if the choice is one of the four option
    if choice in('1', '2', '3', '4'):
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
        except valueError:
            print("invalid number.please enter a number.")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "==", sub(num1,num2))
        elif choice == '3':
            print(num1,"*", num2, "==", mul(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "==", div(num1, num2))
        # check if user want another calculation
        #break the while loop if answer is no
        next_calculation = input("let's do an another calculation?(yes/no):")
        if next_calculation == "no":
                break
        else:
            print("invalid input")
        
    
