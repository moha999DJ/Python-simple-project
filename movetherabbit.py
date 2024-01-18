n1=["🌲", "🌲", "🌲"]
n2=["🌲", "🌲", "🌲"]
n3=["🌲", "🌲", "🌲"]
print(f"""Welcome to game move the rabbit 
      {n1}
      {n2}
      {n3}
      where you should the rabbit go ?""")
rabbit=int(input("Please choose a raw and a column :"))
if rabbit==11:
    #use a simple method
    n1[0]="🐇"
    print(f"{n1}\n{n2}\n{n3}")
elif rabbit==12:
    #useing insert for add a rabbit in the list
    n1.insert(1,"🐇")
    #after the insert i delete last element of the list by using 'del'
    del n1[3]
    print(f"{n1}\n{n2}\n{n3}")
elif rabbit==13:
    n1.insert(2,"🐇")
    del n1[3]
    print(f"{n1}\n{n2}\n{n3}")
elif rabbit==21:
     n2.insert(0,"🐇")
     del n2[3]
     print(f"{n1}\n{n2}\n{n3}")
elif rabbit==22:
     n2.insert(1,"🐇")
     del n2[3]
     print(f"{n1}\n{n2}\n{n3}")
elif rabbit==23:
     n2.insert(2,"🐇")
     del n2[3]
     print(f"{n1}\n{n2}\n{n3}") 
elif rabbit==31:
     n3.insert(0,"🐇")
     del n3[3]
     print(f"{n1}\n{n2}\n{n3}")
elif rabbit==32:
     n3.insert(1,"🐇")
     del n3[3]
     print(f"{n1}\n{n2}\n{n3}")
elif rabbit==33:
     n3.insert(2,"🐇")
     del n3[3]
     print(f"{n1}\n{n2}\n{n3}")
else:
   print("Wrong answer")