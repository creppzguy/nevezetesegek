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
    o=input("Add meg az az országnevét ")
    if o == "Horvátország":
        print("Plitvicei Tavak Nemzeti Park")
    elif o == "Görögország":
        print("Santorini, természetes medence")
    elif o == "Kambodzsa":
        print("Agkor Thom, Baphuon templom")
    elif o == "Japán":
        print("1: Nishinomaru Kert")
        print("2: Arany Pavilon")
        print("3: Himeji Kastély")
        print("4: Dōgo onsen ")
        print("5: Tokió Torony")
        j=input("Válasz a nevezetességek közül ")
        if j == "1":
            print("Nem")
        elif j == "2":
            print("Lehetetlen")
        elif j == "3":
            print("Dehogy")
        elif j == "4":
            print("Semmiképp")
        elif j == "5":
            print("Semmiféleképpen")
elif v == "2":
    e=input("Add meg mikor készült az építmény: ")
    if e == "1949":
        print ("Plitvicei Tavak Nemzeti Park")
    
elif v == "3":
    print("Talán")
