<<<<<<< HEAD
'''Given a set called ‘my_set’, perform the operations described in the comments.'''
def main():
    my_set = set([1, 3, 2, 4, 1, 3, 3, 0])
    
    # add multiple elements
    my_set.update([10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
    
    # delete elements
    my_set.discard(2)
    my_set.discard(3)
    
    li = list(my_set)
    li.sort()

    print(li)
    return 0

if __name__ == '__main__':
    main()
=======
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
>>>>>>> master
