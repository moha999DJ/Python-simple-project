import random
choose=[]
game=["Rock", "Paper", "Scissors"]
#i use random choice for make the game equal :)
bot=random.choice(game)
Rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
print("""Welcome to Rock,Paper,Scissors game: 
    ⠀⠀⠀⠀⠀⣠⡴⠖⠒⠲⠶⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠖⠒⢶⣄⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢀⡾⠁⠀⣀⠔⠁⠀⠀⠈⠙⠷⣤⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⠀⠀⠀⢀⡿⠀⠀⠀⠀⠀⠀⠀
    ⣠⠞⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⠈⢿⡀⢠⡶⠒⠳⠶⣄⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⣰⠏⠀⢀⣤⣤⣄⡀⠀⠀
    ⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠛⠛⠃⠸⡇⠈⣇⠸⡇⠀⠀⠀⠘⣇⠀⠀⣠⡾⠁⠀⠀⠀⢀⣾⣣⡴⠚⠉⠀⠀⠈⠹⡆⠀
    ⣹⡷⠤⠤⠤⠄⠀⠀⠀⠀⢠⣤⡤⠶⠖⠛⠀⣿⠀⣿⠀⢻⡄⠀⠀⠀⢻⣠⡾⠋⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠀⠀⢀⣠⡾⠃⠀
    ⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡤⠖⠋⢀⣿⣠⠏⠀⠀⣿⠀⠀⠀⠘⠉⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀⠀⣠⠶⠋⠁⠀⠀⠀
    ⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠀⠀⠀⢀⣴⡿⠥⠶⠖⠛⠛⢶⡄
    ⠀⠉⢿⡋⠉⠉⠁⠀⠀⠀⠀⠀⢀⣠⠾⠋⠀⠀⠀⠀⢀⣰⡇⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⢀⣠⠼⠃
    ⠀⠀⠈⠛⠶⠦⠤⠤⠤⠶⠶⠛⠋⠁⠀⠀⠀⠀⠀⠀⣿⠉⣇⠀⡴⠟⠁⣠⡾⠃⠀⠀⠀⠀⠀⠈⠀⠀⠀⣀⣤⠶⠛⠉⠀⠀⠀
    ⠀⠀⠀⠀⢀⣠⣤⣀⣠⣤⠶⠶⠒⠶⠶⣤⣀⠀⠀⠀⢻⡄⠹⣦⠀⠶⠛⢁⣠⡴⠀⠀⠀⠀⠀⠀⣠⡶⠛⠉⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢀⡴⠋⣠⠞⠋⠁⠀⠀⠀⠀⠙⣄⠀⠙⢷⡀⠀⠀⠻⣄⠈⢷⣄⠈⠉⠁⠀⠀⠀⢀⣠⡴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢀⡾⠁⣴⠋⠰⣤⣄⡀⠀⠀⠀⠀⠈⠳⢤⣼⣇⣀⣀⠀⠉⠳⢤⣭⡿⠒⠶⠶⠒⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢸⠃⢰⠇⠰⢦⣄⡈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠛⠓⠲⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠸⣧⣿⠀⠻⣤⡈⠛⠳⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠈⠹⣆⠀⠈⠛⠂⠀⠀⠀⠀⠀⠀⠈⠐⠒⠒⠶⣶⣶⠶⠤⠤⣤⣠⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠈⠻⣦⣀⠀⠀⠀⠀⠐⠲⠤⣤⣀⡀⠀⠀⠀⠀⠀⠉⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⠤⠤⠤⠶⠞⠋⠉⠙⠳⢦⣄⡀⠀⠀⠀⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⠦⠾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        
        """)
# Here i use "entre" as input of the user so he will choise between read the rules or directly start the game
entre=input("Press enter to continue of type (Help) for read the rules: ")
# dott lower for make the inputs lowers letters
if entre.lower()=="help":
    print("""
          *******THE RULES********
          1)You chose and the computre chose
          2)Rock smashes Scissors==>Rock win
          3)Scissors cuts Paper ==>Scissor win
          4)Paper covers Rock ===>Paper win
          """)   
# the input "choose" here the user will choose one of the choises 
choose=input("Please chose (Rock ,Paper, Scissors) :").capitalize()
# if the user enter a word or somthing which is not in the list of "game" 
if choose not in game:
    print(f"You enter {choose} which is not from the choises")
elif (
    (choose==game[0] and bot==game[0])
    or
    (choose==game[1] and bot==game[1])
    or
    (choose==game[2] and bot==game[2])
):
    if choose==game[0] and bot==game[0]:
     print(f"Your choise is {choose}\n{Rock}")
     print(f"The computre chose {bot}\n{Rock}") 

    elif choose==game[1] and bot==game[1]:
     print(f"Your choise is {choose}\n{Paper}") 
     print(f"The computre chose {bot}\n{Paper}")
    elif choose==game[2] and bot==game[2]:
     print(f"Your choise is {choose}\n{Scissor}") 
     print(f"The computre chose {bot}\n{Scissor}")
    print("tie")
elif (
    (choose==game[0] and bot==game[1])
    or
    (choose==game[1] and bot==game[2])
    or
    (choose==game[2] and bot==game[0])
):
    if choose==game[0] and bot==game[1]:
     print(f"Your choise is {choose}\n{Rock}")
     print(f"The computre chose {bot}\n{Paper}") 

    elif choose==game[1] and bot==game[2]:
     print(f"Your choise is {choose}\n{Paper}") 
     print(f"The computre chose {bot}\n{Scissor}")
    elif choose==game[2] and bot==game[0]:
     print(f"Your choise is {choose}\n{Scissor}") 
     print(f"The computre chose {bot}\n{Rock}")
    print("You lose")
elif (
    (choose==game[0] and bot==game[2])
    or
    (choose==game[1] and bot==game[0])
    or
    (choose==game[2] and bot==game[1])
):
    if choose==game[0] and bot==game[2]:
     print(f"Your choise is {choose}\n{Rock}")
     print(f"The computre chose {bot}\n{Scissor}") 

    elif choose==game[1] and bot==game[0]:
     print(f"Your choise is {choose}\n{Paper}") 
     print(f"The computre chose {bot}\n{Rock}")
    elif choose==game[2] and bot==game[1]:
     print(f"Your choise is {choose}\n{Scissor}") 
     print(f"The computre chose {bot}\n{Paper}")     
    print("You win")
    
else:
    print(f"{choose} is not from the choices")