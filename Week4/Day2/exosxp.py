#Exercice 1
my_fav_numbers={7, 14, 21, 30, 89}
my_fav_numbers.add(2017)
my_fav_numbers.add(2019)
my_fav_numbers.remove(2019)
print(my_fav_numbers)
friend_fav_numbers={15, 25, 99, 2022}
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#Exercice 2
# Values can't be added to a Tuples! but we can remove values

#Exercice 3
basket=["Banana", "Apples", "Orange", "Blueberries"]
print(basket)
basket.remove("Banana")
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
basket.append("Apples")
print(basket)
#print(counter("Apples"))#non terminé

#Exercice 4
#ex de float: 3.14, 15.2

#Exercice 5
#for number in range(1, 20) :
#    print(number)
#for number in range(1, 21) :
 #   print(number)
#
#Exercice 6
#name="NEYA"
#uname=input(print("Enter your name please:"))
#print(uname)
#while name!=uname:
#    uname=input(print("Enter your name please:"))

#Exercice 7


#Exercice 8
print("You can type quit to stop")
saisipizza={"dark"}
pizza=input(print("Enter a serie of Pizza"))
#pizza=input(print("Enter a serie of Pizza"))
while pizza!="quit":
    saisipizza.add(pizza)
    pizza=input(print("Enter a serie of Pizza"))
    
print(saisipizza)
