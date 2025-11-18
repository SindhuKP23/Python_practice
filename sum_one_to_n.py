#Print the sum of all niumbers from 1 to n

sum = 0
num = int(input("Enter a number: "))
for i in range (1, num+1):
    sum += i
print(f"The sum of numbers from 1 to {num} is {sum}")