f = open("g.txt", "r") 
#print(f.read())
nagylista=[]
for sor in f:
    kislista=sor[:-1].split(";")
    nagylista.append(kislista)
f.close()
#Menü rendszer
print(1.Menü pont)
print(2.menü pont)
print(3.Menü pont)
print(4.Menü pont)
print(4.Menü pont)
