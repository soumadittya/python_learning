# loop using list comprehension

# List comprehension offers a shorter syntax when you want to
# create a new list based on the values of an existing list.

list1 = ['sudipta', 'uttam', 'soumadittya', 'ghosh']
[print(x) for x in list1]

# Example: making a duplicate list
# using list comprehension
cars = ['bmw', 'mercedes', 'honda', 'ford']
new_cars = [x for x in cars]
print(new_cars)

# Example: create a list only fruits starting with 'a' from another list
# using list comprehension
fruits = ['mango', 'apple', 'appricot', 'kiwi', 'cherry', 'banana']
new_fruits = [x for x in fruits if x[0] == 'a']
print(new_fruits)