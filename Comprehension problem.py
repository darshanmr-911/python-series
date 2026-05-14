'''List Manipulation:
Create a list of Kannada foods. Use list comprehension to create a new list where each food name is in uppercase.'''

food=["Dosa","masala dosa","bisibele bath","mudde"]
kannada_foods=[foods.upper() for foods in food]
print(kannada_foods)
print()

'''Sum of Prices:
Create a dictionary of 5 items with their prices. Write a program that calculates the total price of all items using a for loop.'''

price={"onion":80,"tomoto":60,"banana":60,"apple":100,"pineapple":80}
total=0
for items in price.values():
    total+=items
print("Total price of the 5 items:",total)
print()

'''List of Squares:

Create a list of numbers from 1 to 10. Use list comprehension to generate a list of their squares.'''
sq=[1,2,3,4,5,6,7,8,9,10]
list_sq=[square**2 for square in sq]
print(list_sq)
print()

'''Student Data Task:

Create a list of 3 dictionaries, where each dictionary contains the name, age, and marks of a student. Loop through the list and print each student's information.'''
students=[{"name":"darshan","age":25,"marks":85},
          {"name":"pavan","age":27,"marks":90},
          {"name":"prathibha","age":37,"marks":95}]
for student in students:
    print(student)
print()

'''Dictionary Comprehension:

Create a dictionary where the keys are Kannada cities, and the values are their populations. Use dictionary comprehension to filter out cities with populations below 10 lakhs.'''
city={"Bengaluru":12000000,"Mysuru":1500000,"Hubli":900000,"Belagavi":800000,"Mangalore":700000}
city_population={city_name: population for city_name, population in city.items() if population >= 1000000}
print(city_population)
print()

'''Nested List Challenge: Write a Python program that takes a list of lists (a 2D list) as input and:

Prints the entire matrix row by row.
Prints the sum of each row in the matrix.'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    print("Row Matrix:",row)
print()
for add in matrix:
    print("Sum of the matrix is:",sum(add))
