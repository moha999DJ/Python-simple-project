import random
import string
strings=string.digits+string.punctuation
print("Welcome to my app ")
user_name=input("Please enter your username :")
pure_user=""
for password in user_name:
    if password not in strings:
     pure_user+=password
     sugg=random.choices(strings,k=random.randint(1,8))
     sugg_password=[pure_user]+sugg
     random.shuffle(sugg_password)      
print(f"\nThis is your pure username :{pure_user}\n")
print(f"The password you can use is : {"".join(sugg_password)} ")
