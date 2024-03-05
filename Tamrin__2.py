while True :
    a=input("select an operation (variz,bardasht,check inventory):")
    s=0
    if a=="variz" :
        b=float(input("enter a amount of money:"))
        s+=b
        c=input("do you want to see a new inventory?(Yes,NO):")
        if c=="Yes" :
            print(f"result{s}:")
        elif c=="No" :
            print("end!")
    elif a=="bardasht" :
        b=float(input("enter a amount of money:"))
        s-=b
        c=input("do you want to see a new inventory?(Yes,NO):")
        if c=="Yes" :
            print(f"result{s}:")
        elif c=="No" :
            print("end!")
    elif a=="check inventory" :
        print(f"your inventory{s}:") 
    else :
        break
    print("thank for your use!") 