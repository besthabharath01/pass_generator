a=float(input("enter 1st number:"))
b=float(input("enter 2nd number:"))
while True:
    x=int(input("enter choice: 1 for addition (or) 2 for subtraction (or) 3 for multiclation (or) 4 for division (or) 5 for exit:"))
    if x==1:
        addn=a+b
        print(addn)
    elif x==2:
        sub=a-b
        print(sub)
    elif x==3:  
        mul=a*b
        print(mul)
    elif x==4:
        div=a/b
        print(div)
    elif x==5:
        break
    else:
        print("enter valid number")