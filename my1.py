a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("Enter 1 for addition\n2 for subtraction\n3 for multiplication\n 4 for division:")

n=int(input("Enter your choice:"))
if n==1:
    print("addition =",a+b)
elif n==2:
    print("subtraction =",a-b)
elif n==3:
    print("multiplication =",a*b)
elif n==4:
    print("division =",a/b)
