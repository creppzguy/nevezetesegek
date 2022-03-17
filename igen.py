f = open("g.txt", "r") 
print(f.read())
for sor in f:
    idő = input()
    print("Mikor jött létre?: " + idő)
