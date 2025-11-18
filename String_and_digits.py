#Check if a string contains only digits

digits = "0123456789"
num = input("Enter a character: ")
if num in digits:
    print(f"{num} is a digit")
else:
    print(f"{num} is not between 0-9")