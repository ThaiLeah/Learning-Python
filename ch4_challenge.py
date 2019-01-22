#Python Coding Challenge Ch.4

#1 Write a function that takes a number as an input and returns that
# number squared.

def squared(x):
    """Returns x squared.
        :param x: int.
        :return: int value squared
    """
    return x**2

print(squared(2))

#2 Create a function that creates a string as a parameter and prints it.

def print_string(string):
    """Print the inputted string.
        :param string: "string".
        :return: string value printed.
    """
    print(string)

print_string("Fabulous")

#3 Write a function that takes three required parameters and two optional
# parameters.

def customer_info(name, email, age, phone=1111111111, race="unknown"):
    """Gathers customer info
        :param name: string.
        :param email: string.
        :param age: int.
        :param phone: int.
        :param race: string.
        :return: thank you message.
    """
    print("Thank you for participating")

customer_info("Thai", "thaicat.xo@gmail.com", 24)

#4 Write a program with to functions. The first function should take an integer
# as a parameter and return the result of the integer divided by 2. The second
# function should take an integer as a parameter and return the result of the
# integer multiplied by 3. Call the first function, save the result as a variable
# and pass it as a parameter to the second function

def int_divide(int):
    """Returns an integer divided by 2
        :param int:int.
        :return: integer divided by 2.
    """
    return int/2

def int_multiply(int_m):
    """Returns an integer multiplied by 4
        :param int_m: int.
        :return intege multiplied by 4
    """
    return int_m * 4

print(int_divide(4)) # or y = int_divide(4)
result = int_divide(4) # z = int_multiply(y)
print(int_multiply(result)) # print(z)

#5 Write a function that converts a string to a float and returns the result.
# use exception handling to catch the exception that could occur.

def convert_string(string):
    """Converts string to float
        :param string: string.
        :error: a number must be entered.
    """
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float")

c = convert_string("55.0")
print(c)

# 6 Add a docstring to all the functions you wrote in 1-5


