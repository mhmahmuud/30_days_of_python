# Topic : functions
# Exercise 8-1
# 8-1. Message: Write a function called display_message() that prints one sentence 
# telling everyone what you are learning about in this chapter. Call the function, 
# and make sure the message displays correctly.

def display_message():
    """
    Display a simple message.
    """
    message = "i am learning to write functions, which are named blocks of code that are designed to do one specific job."
    return message
print(display_message())

# Exercise 8-2
# Favorite Book: Write a function called favorite_book() that accepts one 
# parameter, title. The function should print a message, such as One of my 
# favorite books is Alice in Wonderland. Call the function, making sure to 
# include a book title as an argument in the function call
def favorite_book(title):
    message = "One of my favorite books is {}".format(title)
    return message

print(favorite_book("Alice in Wonderland"))

# Exercise 8-3
# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the 
# text of a message that should be printed on the shirt. The function should print 
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the 
# function a second time using keyword arguments
def make_shirt(size,text_print):
    return f"The size of the shirt is {size} and the text to be printed is {text_print}."

print(make_shirt(23,"abba"))

# Exercise 8-4
# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large 
# by default with a message that reads I love Python. Make a large shirt and a 
# medium shirt with the default message, and a shirt of any size with a different 
# message.
def make_shirt(text_print,size="large"):
    return f"The size of the shirt is {size} and the text to be printed is {text_print}."

print(make_shirt("I love Python"))
print(make_shirt("meidum","I love Python"))

# Exercise 8-5
# 8-5. Cities: Write a function called describe_city() that accepts the name of 
# a city and its country. The function should print a simple sentence, such as 
# Reykjavik is in Iceland. Give the parameter for the country a default value. 
# Call your function for three different cities, at least one of which is not in the 
# default country.
def describe_city(city,country="Nigeria"):
    return f"{city} is in {country}"
print(describe_city("Kano"))
print(describe_city("Abuja"))
print(describe_city("Accra","Ghana"))
print(describe_city("Niamey","Niger"))
print(describe_city("Kigali","Rwanda"))

# Exercise 8-6
# 8-6. City Names: Write a function called city_country() that takes in the name 
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the 
# values that are returned
def city_country(city,country):
    return f"{city}, {country}"

print(city_country("Kigali","Rwanda"))
print(city_country("Accra","Ghana"))
print(city_country("Abuja","Nigeria"))

# Exercise 8-7
# 8-7. Album: Write a function called make_album() that builds a dictionary 
# describing a music album. The function should take in an artist name and an 
# album title, and it should return a dictionary containing these two pieces of 
# information. Use the function to make three dictionaries representing different 
# albums. Print each return value to show that the dictionaries are storing the 
# album information correctly.
# Use None to add an optional parameter to make_album() that allows you to 
# store the number of songs on an album. If the calling line includes a value for 
# the number of songs, add that value to the album’s dictionary. Make at least 
# one new function call that includes the number of songs on an album.
def make_album(album_name,album_title,num_of_songs=None):
    if num_of_songs:
        album = {"album_name":album_name,"album_title":album_title,"num_of_songs":num_of_songs}
    else:
        album = {"album_name":album_name,"album_title":album_title}
    return album

print(make_album("Common Person","African Giant"))
print(make_album("Yoga","Rora"))
print(make_album("Future","Warr",23))

# Exercise 8-8
# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that 
# information, call make_album() with the user’s input and print the dictionary 
# that’s created. Be sure to include a quit value in the while loop.
def make_album(album_name,album_title,num_of_songs=None):
    if num_of_songs:
        album = {"album_name":album_name,"album_title":album_title,"num_of_songs":num_of_songs}
    else:
        album = {"album_name":album_name,"album_title":album_title}
    return album

while True:
    print("\nPlease tell me your album name:")
    print("(enter 'q' at any time to quit)")
 
    album_name = input("Album name: ")
    if album_name == 'b':
        break
 
    album_title = input("Album title: ")
    if album_title == 'b':
        break

# Exercise 8-9
# 8-9. Messages: Make a list containing a series of short text messages. Pass the 
# list to a function called show_messages(), which prints each text message.
def show_messages(message_list):
    for message in message_list:
        print(message)

print(show_messages(["good fellow","smart fellow","brilliant fellow"]))


# Exercise 8-10
# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
# Write a function called send_messages() that prints each text message and 
# moves each message to a new list called sent_messages as it’s printed. After 
# calling the function,  print both of your lists to make sure the messages were 
# moved correctly
def send_messages(message_list):
    sent_message = []
    for message in message_list:
        print(message)
        sent_message.append(message)
    return f"message_list:{message_list}, sent_message:{sent_message}"
print(send_messages(["good fellow","smart fellow","brilliant fellow"]))

# Exercise 8-11
# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the 
# function send_messages() with a copy of the list of messages. After calling the 
# function, print both of your lists to show that the original list has retained its 
# messages.
send_copy = send_messages(["intelligent fellow","Great fellow","Exraordinary fellow","Nice fellow"])
print("send_copy :- ", send_copy)

# Exercise 8-12
# 8-12. Sandwiches: Write a function that accepts a list of items a person wants 
# on a sandwich. The function should have one parameter that collects as many items 
# as the function call provides, and it should print a summary of the sandwich that’s 
# being ordered. Call the function three times, using a different number of arguments each time
def sandwiches(*sandwiches):
    print("The Summary of sandwiches ordered")
    for sandwiche in sandwiches:
        print(sandwiche)
print(sandwiches("cheese","burger","snacks"))
print(sandwiches("salad","pepper","fish"))
print(sandwiches("meat","burger","ketchup"))


# Exercise 8-13
# 8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a 
# profile of yourself by calling build_profile(), using your first and last names 
# and three other key-value pairs that describe you
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('ISHAQ', 'HASSAN',field='Software Engineering',city='Kano', country='Nigeria')
print(user_profile)    

# Exercise 8-14
# 8-14. Cars: Write a function that stores information about a car in a dictionary. 
# The function should always receive a manufacturer and a model name. It 
# should then accept an arbitrary number of keyword arguments. Call the function 
# with the required information and two other name-value pairs, such as a 
# color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was 
# stored correctly.
def make_car(*args, **kwargs):
    car_info = {}
    car_info["manufacturer"] = args[0]
    car_info["model"] = args[1]
    
    for key, val in kwargs.items():
        car_info[key] = val
    
    return car_info

print(make_car('subaru', 'outback', color='blue', tow_package=True))

# Exercise 8-15
# 8-15. Printing Models: Put the functions for the example printing_models.py in a 
# separate file called printing_functions.py. Write an import statement at the top 
# of printing_models.py, and modify the file to use the imported functions
from printing_models import *
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# Exercise 8-16
#8-16
# 8-16. Imports: Using a program you wrote that has one function in it, store that 
# function in a separate file. Import the function into your main program file, and 
# call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *
import printing_models
from printing_models import print_models
from printing_models import print_models as fn
import printing_models as mn
from printing_models import *
