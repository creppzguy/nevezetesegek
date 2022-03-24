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
print("3 3.Menü pont")
v=input("Add meg a válaszott menü pont jelét ")
if v == "1":
    o=input("Adj meg egy országnevet ")
    if o == "Horvátország":
        print("Plitvicei Tavak Nemzeti Park")
elif v == "2":
    print("Igen")
elif v == "3":
    print("Talán")
