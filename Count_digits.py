#Program to count the number of digits in a number

num = int(input("Enter a number:"))
count =0
while num>0:
    num = num//10
    count+=1
print(f"Total count of digits from {num} is :{count}")