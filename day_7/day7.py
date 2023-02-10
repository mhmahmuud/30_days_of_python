### Day 7: 30 Days of python programming
##Exercises: Level 1

# sets
it_companies = {'Facebook', 'Google',
                 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Question 1
# Find the length of the set it_companies
print(len(it_companies))

# Question 2
# Add 'Twitter' to it_companies
it_companies.add('Twitter')

# Question 3
# Insert multiple IT companies at once to the set it_companies
it_companies.update(["Snapchat","2go","Samsung"])

# Question 4
# Remove one of the companies from the set it_companies
it_companies.remove('Twitter')

# Question 5
# What is the difference between remove and discard
""" both remove() and discard() are used to remove an item in a sets,
 remove() returns errors if the item to be removed is not in the sets 
 while discard() return nothing if the item to be removed is not in the sets"""

# Exercises: Level 2
# Question 1
# Join A and B
A.union(B)

# Question 2
# Find A intersection B
A.intersection(B)

# Question 3
# Is A subset of B
A.issubset(B)

# Question 4
# Are A and B disjoint sets
A.isdisjoint(B)

# Question 5
# Join A with B and B with A
A.union(B) and B.union(A)

# Question 6
# What is the symmetric difference between A and B
A.symmetric_difference(B)

# Question 7
# Delete the sets completely
del A,B

# Exercises: Level 3
<<<<<<< HEAD
# Question 1
# Convert the ages to a set and compare the length 
# of the list and the set, which one is bigger?
age_in_sets = set(age)
len(age_in_sets) > len(age) # False
len(age) > len(age_in_sets) # True

# Question 2
# Explain the difference between the following
# data types: string, list, tuple and set
"""
    tuple is immutable which means it cannot be change once created,
    list and set are mutable which means it can be change once created
    string is mutable with the string function "str.replace()" and it is immutable through indexing assignment "str[index]",
    string, tuple and list are ordered while set is unordered 
"""

# Question 3
# "I am a teacher and I love to inspire and teach people."
#  How many unique words have been used in the sentence?
#  Use the split methods and set to get the unique words.
no_of_words_used = len(" I am a teacher and I love to inspire and teach people".split())
 
=======
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# Explain the difference between the following data types: string, list, tuple and set
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
>>>>>>> 1c0732d05bc2c0323ece825e5132c49ffe0d52a8
