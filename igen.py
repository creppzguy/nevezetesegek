f = open("g.txt", "r") 
#print(f.read())
nagylista=[]
for sor in f:
    kislista=sor[:-1].split(";")
    nagylista.append(kislista)
f.close()

#Menü rendszer
print("1= Országnév")
print("2= Építmény keletkezése")
print("3.Menü pont")
v=input("Add meg a válaszott menü pont jelét ")
if v == "1":
    orszag=input("Adj meg egy országot")
    for i in range(0,len(nagylista)):
        if orszag == nagylista[i][1]:
            print(nagylista[i][0])
            print(nagylista[i][2])
#elif v == "2":
    
#elif v == "3":
    print("Talán")
