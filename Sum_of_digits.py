#Program to sum the digits of a number

num = int(input("Enter a number: "))
sum =0
while num > 0:
    sum += num %10 #3+2+1
    num = num//10
print(f"The sum of digits is :{sum}")