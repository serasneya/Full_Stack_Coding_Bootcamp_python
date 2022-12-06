mot = str(input("Enter a string: "))
if len(mot)>10:
    print("string too long")
else:
    print("string not long enough")
#affichage premier mot
print(str(mot)[0])
#affichage dernier mot
print(str(mot)[len(mot)-1])
i=len(mot)
for i in range(0, len(mot)):
    print(str(mot)[i])