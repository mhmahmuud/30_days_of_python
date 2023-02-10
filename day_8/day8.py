### Day 8: 30 Days of python programming
## Exercise: Level 1
# Question 1
# Create an empty dictionary called dog
dog = {}

# Question 2
# Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "jacki"
dog["color"] = "brown"
dog["breed"] = "Hound Group"
dog["legs"] = 4
dog["age"] = 3

# Question 3
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {"first_name":"Isma\'il",
           "last_name":"Ahmad",
           "gender":"Male",
           "marital status":"Single",
           "skills":["Writting","Poet","Typing","Art"],
           "country":"Nigeria",
           "city":"kano state",
           "address":"Hotoro North"
           }

# Question 4
# Get the length of the student dictionary
print(len(student))

# Question 5
# Get the value of skills and check the data type, it should be a list
print(type(student["skills"]))

# Question 6
# Modify the skills values by adding one or two skills
student["skills"].append("Painting")
student["skills"].append("Coding")

# Question 7
# Get the dictionary keys as a list
student.keys()

# Question 8
# Get the dictionary values as a list
student.values()

# Question 9
# Change the dictionary to a list of tuples using items() method
student.items()

# Question 10
# Delete one of the items in the dictionary
del student["marital status"]

# Question 11
# Delete one of the dictionaries
del dog
