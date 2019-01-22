# python challenge ch5

# 1 create a list of your favorite musicians

fav_musicians = ['drake', 'rihanna', 'cardi b']

print(fav_musicians)

# 2 create a list of tuples, with each tuple containing the longitude and latitude of somewhere you lived or visited

locations_lived = []

chicago = (41.8781, 87.6298,)
atlanta = (33.753746, -84.386330,)

locations_lived.append(chicago)
locations_lived.append(atlanta)

print(locations_lived)

# 3 create a dictionary that contains different attributes about you: height, fav color, fav author, etc

about_me = {'height': '5 feet 5 inches', 'fav_color': 'black', 'fav_author': 'jk rowling'}

print(about_me)

# 4 write a program that lets the user ask your height, fav color, or fav author and returns the result from the dictionary you created in question 3


me = {'height': '5 feet 5 inches', 'fav_color': 'black', 'fav_author': 'jk rowling'}

answer = input('type height, fav_color,or fav_author:')

if answer in me:
    result = me[answer]
    print(result)

# 5 create a dictionary mapping your favorite musicians to a list of your favorite songs by them

fav_music = {'drake': 'lose you', 'cardi b': 'bodak yellow', 'rihanna': 'rude boy'}

print(fav_music)

# 6 lists,tuples, and dictionaries are just a few of the containers built into Python. Research python sets ( a type of container). When would you use a set?

print('a set is used to carry out mathematical set operations such as union, intersection, difference, and systematic difference')

