#Calculator 2+2 is 4
print("quick mafs")
print("ez mafs")
print("")
print("select an operation")
print("choice 1 = addition")
print("choice 2 = subtraction")
print("choice 3 = multiplication")
print("choice 4 = divition")

choice = input("Enter what function you wanna use:")
num1 = int(input("Enter your first number:"))
num2 = int(input("Enter the second number"))

if choice == '1':
    print(num1,"+"num2,"=",add(num1+num2))
elif choice =='2':
    print(num1,"-"num2,"=",subtract(num1+num2))
elif choice =='3':
    print(num1,"*"num2,"=",multiply(num1+num2))
elif choice =='4':
    print(num1,"/"num2,"=",divide(num1+num2))
else
    print(value has no function)
