#Set Operations:

#Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.
my_fruit={"apple","banana","mango"}
frd_fruit={"mango","orange","grapes"}
#Find the union, intersection, and difference between the two sets.
print(my_fruit&frd_fruit)
print(my_fruit|frd_fruit)
print(my_fruit-frd_fruit)
#Add a new fruit to your set.
my_fruit.update("kiwi")
print(my_fruit)
#Remove a fruit from your set using both remove() and discard(). What happens when the fruit doesn’t exist?
print(my_fruit.remove("apple"))
print(my_fruit.discard("banana"))
