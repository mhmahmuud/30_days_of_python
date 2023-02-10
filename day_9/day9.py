### Day 9: 30 Days of python programming
## Exercise: Level 1
# Question 1
# Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback:
# You are old enough to drive. 
# If below 18 give feedback to wait for the
# missing amount of years. Output:

age = int(input("Enter your age: "))
if age >= 18 :
    print("You are old enough to learn to drive.")
else:
    print("You need {} more years to learn to drive".format(18-age))

# Question 2
# Compare the values of my_age and your_age using if … else.
# Who is older (me or you)? Use input(“Enter your age: ”) to get
# the age as input. You can use a nested condition to print 'year' 
# for 1 year difference in age, 'years' for bigger differences, and
# a custom text if my_age = your_age
my_age = int(input("Enter your age: "))
your_age = int(input("Enter your age: "))
if my_age >=0 and your_age >=0:
    if my_age > your_age:
        print("I am {} year(s) older than you.".format(my_age - your_age))
    elif your_age == my_age:
        print("We both have thesame age {} year(s).".format(your_age))
    else:
        print("You are {} years older than me.".format(your_age - my_age))
else:
    print("number below or to zero")
# Question 3
# Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b.
num_one = int(input("Enter number one: "))
num_two = int(input("Enter number two: "))
if num_one > num_two:
    print("{} is greater than {}".format(num_one,num_two))
elif num_two > num_one:
    print("{} is greater than {}".format(num_two,num_two))
else:
    print("{} is equal to {}".format(num_one,num_two))


## Exercises: Level 2
# Question 1
# Write a code which gives grade to students according to theirs scores:
score = int(input("Enter your score: "))
if score > 0:
    if score >= 80:
        print("Your grade is A.")
    elif score >=70 :
        print("Your grade is B.")
    elif score >= 60:
        print("Your grade is c.")
    elif score >= 50:
        print("Your grade is D.")
    else:
        print("Your grade is F.")
else:
    print("score not between 0 to 100")

# Question 2
# Check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, 
# the season is Autumn. December, January or February, 
# the season is Winter. March, April or May, the season 
# is Spring June, July or August, the season is Summer
month = str(input("Enter the month: "))
month = month.lower()
month_list = [
    "january","febuary",
    "march","april","may",
    "june","july","august",
    "september","octomber",
    "november","december"
]
season_dict = {
    "january":"Autumn",
    "febuary":"Autumn",
    "march":"Winter",
    "april":"Winter",
    "may":"Winter",
    "june":"Spring",
    "july":"Spring",
    "august":"Spring",
    "september":"Autumn",
    "octomber":"Winter",
    "november":"Summer",
    "december":"Autumn",
}

if month in month_list:
    print("{}".format(season_dict[month]))
else:
    print("the month is not entered in full")

# Question 3
# The following list contains some fruits:
# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list 
# and print the modified list. If the fruit exists 
# print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = str(input("Enter a fruit: "))
if fruit in fruits:
    print("{}".format(fruit))
else:
    fruits.append(fruit)
    print(fruits)

## Exercises: Level 3
# Question 3
# Check if the person dictionary has skills key,
# if so print out the middle skill in the skills list.
# Check if the person dictionary has skills key, 
# if so check if the person has 'Python' skill and print out the result.
# If a person skills has only JavaScript and React, 
# print('He is a front end developer'), if the person skills has Node, 
# Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, 
# Print('He is a fullstack developer'), else print('unknown title') 
# - for more accurate results more conditions can be nested!
# If the person is married and if he lives in Finland, 
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if "skills" in person:
    print(person["skills"][int(len(person["skills"])/2)])

if "skills" in person:
    if 'Python' in person["skills"]:
        print(person["skills"])

if 'JavaScript' in person["skills"] and 'Node' in person["skills"]:
    print('He is a frontend developer')

if 'Node' in person["skills"] and 'MongoDB' in person["skills"] and 'Python' in person["skills"]:
    print('He is a backend developer')
if 'React' in person["skills"] and  'Node' in person["skills"] and "MongoDB" in person["skills"] :
    print("He is a fullstack developer")

if person["is_marred"] == True:
    print("{} {} lives in {}. He is married.".format(person["first_name"],person["last_name"],person["country"]))
