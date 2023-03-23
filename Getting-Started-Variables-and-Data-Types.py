some_string = "Hello Python"
print(some_string)

a_str = "This is an example of a string in quotes" # In python the word string is abbreviated to str
my_float = 5.5
an_integer = 5 # integer is abbreviated to int
shopping_list = ["apples", "oranges", "pears"]
a_dict = {"userId": "JBloggs"} # dictionary is abbreviated to dict
example_tuple = ("apple", "orange", "pear")
boolean_values = True # boolean is abbreviated to bool

# Strings, like all data types, can be assigned to a variable.


first_name = "Monty"
last_name = "Python"
print(first_name+last_name)

# You can add strings together using variables. This concatenates them.


print(first_name + " " + last_name)

first_name = "John"
surname = "Doe"


#  To include a space, you need to either add it to the beginning or end of your word or add it as a separate string. Fix the sentence below.
print("My first name is {}. My family name is {}".format(first_name, surname))

# If you have multiple variables

firstname = "Jane"
surname = "Doe"

# Some people find this format easier to read.


print(f"My first name is {firstname}. My family name is {surname}")


#Using Number Variables in Strings
my_int = 50
sentence = "The total comes to: "

print(sentence + str(my_int))

# Creating, Reading, Updating and Deleting values in a dictionary

# Create

user = {"first_name":"Ada"}
print(user)

#To read the value associated with a key,
user = {"first_name":"Ada"}
print(user["first_name"])

#Add a key-value
user["family_name"] = "Byron"
print(user)

# To modify a value 
user["family_name"] = "Lovelace"
print(user)

# To remove a key-value pair you use the del statement 
# with the name of the dictionary and the key you want to delete.

del user["family_name"]
print(user)

#Creating, Reading, Updating and Deleting elements in a list

#Create

fruit = ["apples","oranges","bananas"]

#Read

fruit = ["apples","oranges","bananas"]
print(fruit[1])
#You can find the length of a list using len()

len(fruit)
print(len(fruit))

#Update

fruit.append("kiwi")
print(fruit)

#If you want add an element at a specific point in the list 
#you can use the index value with the insert() method.

fruit.insert(2, "passion fruit")
print(fruit)

# If you want to return information which is sorted, 
#but retain the original order of the list, you can use the sorted() function.

print(sorted(fruit))
print(fruit)

#f you want to permanently sort the list, you should use the sort() method.

fruit.sort()

print(fruit)

# Delete

del fruit[1]
print(fruit)

#If you want to use the value after removing 
#it from a list you use the pop() method.

favorite_fruit = fruit.pop()
print(favorite_fruit)
