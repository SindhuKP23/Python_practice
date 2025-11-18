 #Vowel or Consonant

#letter = input("Enetr a letter:")
#if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
    #print(f"{letter} is a Vowel")
#else:
   #print(f"{letter} is a Consonant")

#OR

#letter = input("Enter a letter: ").lower()
#vowels = 'aeiou'
#if letter in vowels:
   # print(f"{letter} is a Vowel")
#else:
 #   print(f"{letter} is a Consonant")

#For DSA Level

vowel = {'a', 'e', 'i', 'o', 'u'}
letter = input("Enter a letter: ")
if letter.lower() in vowel:
    print(f"{letter} is a Vowel")
else:
    print(f"{letter} is a Consonant")





