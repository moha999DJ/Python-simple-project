print("""Welcome to Mohammed Calculator """)
op=int(input("""Please choose a number :
        1-Addition
        2-Multiplication
        3-Subtraction
        4-Division \n"""))
if op==1:
    print("You choose a Addition(+)")
    add1=float(input("Add your fist number :"))
    add2=float(input("add your second number :"))
    summ=float(add1+add2)
    print("result = ",summ)
elif op==2:
    print("You choose a Multiplication(*)")
    mo1=float(input("Add your first number:"))
    mo2=float(input("Add your second number"))
    mul=float(mo1*mo2)
    print("The result =",mul)
elif op==3:
     print("You choose a Subtraction(-)")
     sub1=float(input("Add your first number:"))
     sub2=float(input("Add your second number:"))
     subr=float(sub1-sub2)
     print("The result= ",subr)
elif op==4:
    print("You choose a Division(%)")
    di1=float(input("Add your first number:"))
    di2=float(input("Add your second number:"))
    div=float(di1//di2)
    dive=float(di1%di2)
    print(f"""The result of division is ={div}
    and the rest of division is ={dive}""")
else:
    print(f"{op} is not a number from choises, please try again")