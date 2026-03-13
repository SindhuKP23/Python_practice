#Program to reverse a number

num = int(input("Enter a number: "))
rev = 0
while num>0:
    digit= num%10 #123 = 3+2+1
    rev = digit*10+num
    num = num//10 #123 = 12 - 1 - 0
print(rev)