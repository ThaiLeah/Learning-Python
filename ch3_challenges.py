#Python Chanllenges Chapter 3

#1. Print 3 different strings

print("my name is Thai.")
print("I'm learning Python")
print("I love Python so far")

#2. Write a program that prints a message if a variable is less than 10,
#and a different message if the variable is greather than or equal to 10x

x = 9

if x < 10:
    print("x is less than 10")
else:
    print("x is greater than 10")

#3 write a program that print a message if a variable is less than or equal to
#10, another message if the variable is greater than 10 but less than or equal
#to 25, and another message if the variable is greater than 25

a = 12

if a <= 10:
    print("a is smaller than 10")
elif a > 10 and a <= 25:
    print("a is between 10 and 25")
else:
    print("a is larger than 25")


#4 Create a program  that divides two variables and prints the remainder

20 % 3

#5 Create a program that takes two variables, divides them, and prints the
#quotient

16 // 3

#6 Write a program with a variable age assigned to an integer that prints
# different strings depeneding on what integer age is

age = 24

if age == 18:
    print("Welcome to adulthood")
elif age == 21:
    print("Enjoy a glass of wine")
elif age == 24:
    print("learn to code before 25")
else:
    print("Don't worry, you'll make it")
        
#6 from answers doc

age = 64
retirement = age- 65

if retirement < 10:
    print("You get to retire soon")
else:
    print("You have a long time until you can retire")
