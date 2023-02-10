### Day 12: 30 Days of python programming
## Exercise: Level 1
# Question 1
# Writ a function which generates a six digit/character random_user_id.
#  print(random_user_id()); output: '1ee33d'
from random import random, randint 
def random_user_id():
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    random_user_id = ''
    for i in range(6):
        n = randint(0,61)    
        random_user_id = random_user_id + chars[n]     
    return random_user_id
print(random_user_id())

# Question 2
# Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is 
# the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user()) # user input: 5 5
def user_id_gen_by_user():
    num_of_chars = int(input("Enter a num of characters to be generated: "))
    num_of_IDs = int(input("Enter a num of IDs to be generated: "))
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    random_user_id = ''
    for i in range(num_of_IDs):
        for i in range(num_of_chars): 
            n = randint(0,61)    
            random_user_id = random_user_id + chars[n]
            if  len(random_user_id)== num_of_chars:
                print(random_user_id)
                random_user_id = ""
            else:
                continue
    return random_user_id
print(user_id_gen_by_user())

# Question 3
# Write a function named rgb_color_gen. It will generate 
# rgb colors (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
from random import choice
def random_color():
    levels = range(32,256)
    return "rgb" + str(tuple(choice(levels) for i in range(3)))
print(random_color())

## Exercises: Level 2
# Question 1
# Write a function list_of_hexa_colors which returns any number of 
# hexadecimal colors in an array (six hexadecimal numbers written after 
# #. Hexadecimal numeral system is made out of 16 symbols, 0-9 an   d 
# first 6 letters of the alphabet, a-f. Check the task 6 for output 
# examples).
import random
def list_of_hexa_colors(n):
    list_hexa_colors = []
    for i in range(n):
        color = random.randrange(0, 2**24)
        hex_color = "#" + hex(color)
        list_hexa_colors.append(hex_color)       
    return list_hexa_colors
print(list_of_hexa_colors(4))

# Question 2
# Write a function list_of_rgb_colors which returns any number of RGB 
# colors in an array.
from random import choice
def list_of_rgb_colors(n):
    rgb_list = []
    for i in range(n):
        levels = range(32,256)
        rgb = "rgb" + str(tuple(choice(levels) for i in range(3)))
        rgb_list.append(rgb)
    return rgb_list
print(list_of_rgb_colors(4))

# Question 3
# Write a function generate_colors which can generate any number
# of hexa or rgb colors.
from rgb_hex import list_of_hexa_colors, list_of_rgb_colors
def generate_colors(_str,n):
    if _str.lower() == "hexa":
        return list_of_hexa_colors(n)
    elif _str.lower() == "rgb":
        return list_of_rgb_colors(n)
    else:
        print("invalid rgb and hex color codes!") 

print(generate_colors("hexa",3))
print(generate_colors("Hexa",3))
print(generate_colors("rgb",3))
print(generate_colors("rgb",3))

# Exercises: Level 3
# Question 1
# Call your function shuffle_list, it takes a list as a 
# parameter and it returns a shuffled list


# printing shuffle list
def shuffle_list(lst):
    import random
    # printing list before shuffle
    print("The original list : {}".format(lst))
    random.shuffle(lst)
    
    # return list after shuffle
    return "List 1 after shuffle : {}".format(lst)
print(shuffle_list([6, 4, 8, 9, 10]))



# Question 2
# Write a function which returns an array of seven random 
# numbers in a range of 0-9. All the numbers must be unique.

random.randrange