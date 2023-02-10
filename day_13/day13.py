### Day 13: 30 Days of python programming
### Topic : List Comprehension
## Exercise: Level 1
# Question 1
# Filter only negative and zero in the list using list comprehension
# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_nums = [i for i in numbers if i > 0]
print(filtered_nums)

# Question 2
# Flatten the following list of lists of lists to a one dimensional list :
# list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
one_dimension = [num for row in list_of_lists for col in row for num in col]
print(one_dimension)


# Question 4
# Using list comprehension create the following list of tuples:
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]
list_of_tuples = [str((n,1,n,n*n,n*n*n,n*n*n*n,n*n*n*n*n)) for n in range(11)]
print(list_of_tuples)

# Question 4
# Flatten the following list to a new list:
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
# Soln
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
Flatten_lists = [[col[0].upper(),col[0][:3].upper(),col[-1].upper()]  for row in countries for col in row ]
print(Flatten_lists)

# Alternate Soln 
for row in countries:
    for col in row:
        col = list(col)
        col.insert(1,col[0][:3])
        print(col)
        
# Question 5
# Change the following list to a list of dictionaries:
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], 
# [('Norway', 'Oslo')]]
# output: [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]
lists_dict = [{"country":col[0].upper(),"city":col[-1].upper()}  for row in countries for col in row ]
print(lists_dict)

# Question 6
# Change the following list of lists to a list of concatenated strings:
# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], 
# [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output: ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [fullname[0]+ " " + fullname[-1]  for row in names for fullname in row ]
print(full_names)

# Question 7
# Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, y1, x2, y2: (y2-y1)/(x2-x1)
intercpt = lambda x1, y1, x2, y2: "b = " + str(y1 - slope(x1, y1, x2, y2) * x1)
print(intercpt(2,3,5,5))
