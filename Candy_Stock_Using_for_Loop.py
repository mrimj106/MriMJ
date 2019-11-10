#Progragm printing number of choclate that need and if limit crossed printing out of stock
stock=10
x=input("Enter the number of choclate you want ")
i=1
for m in range(x):
    if i>stock:
        print("We are out of stock now We only had total",i-1,"choclate")
        break
    print ("Choclate")
    i = i + 1
print ("Enjoy your choclate now")
