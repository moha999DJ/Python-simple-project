import random
import string

print("*********Welcome to the Password Generator ! *********")
number_of_characters=int(input("Enter the total number of characters in the password :"))
number_of_letters=int(input("Enter the number of letters in the password :"))
number_of_numbers=int(input("Enter the number of numbers in the password :"))
number_of_symbols=int(input("Enter the number of symbols in the password :"))
#the total number of letters , numbers and symbols
sum_of_numbers=number_of_letters+number_of_numbers+number_of_symbols
#The condition if the total numbers equal the number of characters
if number_of_characters==sum_of_numbers:
    #Make random of letters , numbers and symbols include by inputs condition
    r1=random.choices(string.ascii_letters,k=number_of_letters)
    r2=random.choices(string.digits,k=number_of_numbers)
    r3=random.choices(string.punctuation,k=number_of_symbols)
    #The sum of random kind of each one
    password=r1+r2+r3
    #Shuffle the sum for making a hard and unexpected password 
    random.shuffle(password)

    print(f"The Password is :\n{"".join(password)}")
else:
    print("Invalid input ! , the sum of letters , numbers and symbols doesn't match the number of password")