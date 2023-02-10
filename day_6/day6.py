### Day 6: 30 Days of python programming
##Exercises: Level 1
#Question 1
# Create an empty tuple
empty_tuple = ()
empty_tuple = tuple()

#Question 2
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Aminu","Hamza","Yaseer","Muhammad")
sisters = ("Zainab","Khadijah","Hafsat")
#Question 3
# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

#Question 4
# How many siblings do you have?
print(len(siblings))

#Question 5
# Modify the siblings tuple and add the name of your father and
# mother and assign it to family_members
family_members = siblings + ("Kawu", "maman aminu")

## Exercises: Level 2
#Question 1
# Unpack siblings and parents from family_members
del family_members

#Question 2
# Create fruits, vegetables and animal products tuples. Join the 
# three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Mango","Apple","Banana","Orange","Pine-apple")
vegetables = ("Tomato","Cocumber","Onions","Peper")
animal = ("Cow","Goat","Ram","Camel")
food_stuff_tp = fruits + vegetables + animal

#Question 3
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

#Question 4
# Slice out the middle item or items from the 
# food_stuff_tp tuple or food_stuff_lt list.
food_stuff_tp[int(len(food_stuff_tp)/2)]

#Question 5
# Slice out the first three items and the last three items from 
# food_staff_lt list
food_stuff_lt[3:-3]

#Question 6
# Delete the food_staff_tp tuple completely
del food_stuff_tp

#Question 7
# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries) # False
print('Iceland' in nordic_countries) # True