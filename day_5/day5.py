### Day 5: 30 Days of python programming
## Exercise: Level 1
# Question 1
lst = list()
lst = []

# Question 2
lst = ["item1","item2","item3","item4","item5","item6","item7"]

# Question 3
print(len(lst))

# Question 4
print(lst[0])
print(lst[int(len(lst)/2)])
print(lst[-1])

# Question 5
mixed_data_types = ["Ishaq Hassan", 23, 18.5, "single", "Zawaciki, Kano State"]

# Question 6
it_companies =  ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Question 7
print(mixed_data_types)
print(it_companies)

# Question 8
#print(len(mixed_data_types))
print(len(it_companies))

# Question 9
print(it_companies[0])
print(it_companies[int(len(lst)/2)])
print(it_companies[-1])

# Question 10
it_companies[0] = "Watsapp"

# Question 11
it_companies.append("Instagram")

# Question 12
it_companies.insert(int(len(it_companies)/2),"SnapChat")

# Question 13
it_companies[0].upper()

# Question 14
it_compan = it_companies[0] + "#" + it_companies[1] + "#" + it_companies[2] + "#" + it_companies[3] + "#" + it_companies[4] + "#" + it_companies[5] + "#" + it_companies[6] + "#" + it_companies[7] 

# Question 15
does_IBM_exist = "IBM" in it_companies

# Question 16
it_companies.sort()

# Question 17
it_companies.sort(reverse=True)

# Question 18
it_companies[3:]

# Question 19
it_companies[:-3]

# Question 20
int(len(it_companies))

# Question 21
it_companies.pop(0)

# Question 22
it_companies[4:5]

# Question 23
it_companies.pop(-1)

# Question 24
it_companies.clear()

# Question 25
del it_companies[:]

# Question 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)

# Question 27
full_stack = front_end


## Exercises: Level 2
# Question 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# sort the list and find the min and max age
sorted_ages = sorted(ages)
min_age = min(ages)
max_age = max(ages)

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)

# Find the median age (one middle item or two middle items divided by two)
meadian_age = ages[int(len(ages)/2)]

# Find the average age (sum of all items divided by their number )
average_age = sum(ages) / len(ages)

# Find the range of the ages (max minus min)
age_range = max_age - min_age

# Compare the value of (min - average) and (max - average), use abs() method
abs_value = abs(min_age - average_age) == abs(max_age - average_age)


#Question 3
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

# Find the middle country(ies) in the countries list
mid_countries = countries[int(len(countries)/2)]

# Divide the countries list into two equal lists if 
# it is even if not one more country for the first half.
countries_1st_half = countries[:int(len(countries)/2)]
countries_1st_half = countries[int(len(countries)/2):]

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
# Unpack the first three countries and the rest as scandic countries.
super_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *scandic = super_countries