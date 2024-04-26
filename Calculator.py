print("***********************SIMPLE PYTHON CALCULATOR ****************")

x=input("Enter first number")
y=input("Enter second number")

print("Enter 1 for addition\nEnter 2 for subtraction\nEnter 3 for multiplication\nEnter 4 for division")
choice = int(input("Enter your choice"))

if choice==1:
    print(int(x)+int(y))

elif choice==2:
    print(int(x)-int(y))

elif choice==3:
    print(int(x)*int(y))

elif choice==4:
    print(int(x)/int(y))

else:
    print("Invalid operation")

