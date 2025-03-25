a=int(input("enter a nummber :"))
c=0
for i in range(1,a):
    if a%i==0:
        c+=1


if c>=2:
    print("non prime")
else:
    print("prime")

