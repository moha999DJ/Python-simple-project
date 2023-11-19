import random
print("Welcome to the coin guessing game !")
method=input("""Choose a method to toss the coin :
1-Using random.random()
2-Using random.randint(0,1)
Entre your choise 1 or 2 :""")
face=input("Entre your guess (heads or tails) :")
coin1=random.random()
coin2=random.randint(0,1)
if method=="1":
    if coin1>=0.5:
        thecomputer_result="heads"
        if face.lower()==thecomputer_result:
          print("CONGRATULATIONS YOU WIN ")   
        else:
         print(f"""Sorry you lost
            the computer's toss result is {thecomputer_result}""")
    else:
        thecomputer_result="tails"
        if face.lower()==thecomputer_result:
          print("CONGRATULATIONS YOU WIN ")
        else:
         print(f"""Sorry you lost
            the computer's toss result is {thecomputer_result}""")
elif method=="2":
        if coin2==1:
            thecomputer_result="heads"
            if face.lower()==thecomputer_result:
             print("CONGRATULATIONS YOU WIN ")
            else:
             print(f"""Sorry you lost
            the computer's toss result is {thecomputer_result}""")
        else: 
           thecomputer_result="tails"
           if face.lower()==thecomputer_result:
             print("CONGRATULATIONS YOU WIN ")
           else:
              print(f"""Sorry you lost
              the computer's toss result is {thecomputer_result}""")
else:
   print("You entre a avaible choise !!")