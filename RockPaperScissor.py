import random
toy=random.randint(0,2)
print("""Welcome to game (Rock Paper Scissors) :""")
luck=(input("Please choose a guess (Rock) ,(Paper) or (Scissor) : "))
#each number in order (0 ,1 and 2) equal Rock ,Paper and Scissor
if luck.lower()=="rock":
    if toy==0:
        booot="rock"
        print("DRAW") 
    elif toy==1:
        booot="paper"
        print(f"You lose the boot choose {booot}")
    elif toy==2:
        booot="scissor"
        print("CONGRATULATIONS YOU WIN !!")
elif luck.lower()=="paper":
    if toy==0:
        booot="rock"
        print("CONGRATULATIONS YOU WIN !!")
    elif toy==1:
        booot="paper"
        print("DRAW") 
    elif toy==2:
        booot="scissor"
        print(f"You lose the boot choose {booot}")
elif luck.lower()=="scissor":
    if toy==0:
        booot="rock"
        print(f"You lose the boot choose {booot}")
    elif toy==1:
        booot="paper"
        print("CONGRATULATIONS YOU WIN !!")
    elif toy==2:  
        booot="scissor"
        print("DRAW")
else: 
  print("Selection not found !")