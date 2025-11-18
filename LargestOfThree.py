#Find the largest of 3 numbers 
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
c= int(input("Enter third number: "))
if a>b and a>c:
    print(f"{a} is greater among {b} and {c}")
elif b>a and b>c:
    print(f"{b} is greater among {a} and {c}")
else:
    print(f"{c} is greater among {a} and {b}")
