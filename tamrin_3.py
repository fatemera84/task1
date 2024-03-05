a=int(input("enter a number1 :"))
b=int(input("enter number2 :"))
c=input("enter operation (sum,difference,multiple,divide):")
r=0
if c=="sum":
    r=a+b
elif c=="difference":
    r=a-b
elif c=="multiple":
    if a==0 or b==0 :
        print("zero")
    else:
        r=a*b
elif c=="divide":
    if b==0:
        print("error!")
    else:
        r=a/b
else:
    print("select a correct operation")

print(f"result:{r}")