import random
print("""Welcome to 'Whos's wallet?'
      you will give me a list of names.and i will pick a person to pay """)
names_string=str(input("if you're ready,enter the names sperated by a comma :\n "))
names=[]
names=names_string.split(", ")
name=random.choice(names)
print(f"Please ask {name} to take his wallet out.Dinner is on him")