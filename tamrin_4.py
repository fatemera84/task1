a=float(input("enter a tempeture:"))
b=input("select an operation (FC_CF):")
s=0
if b=="FC" :
    s=(a-32)/1.8
elif b=="CF":
    s=(a*1.8)+32
print(f"result:{s}")