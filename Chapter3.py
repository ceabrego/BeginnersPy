# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 09:03:40 2018

@author: dscabrego
"""
value1 = eval(input('Please enter a number: '))
value2 = eval(input('Please enter another number: '))
sum = value1 + value2
print(value1, '+', value2, '=', sum)
#%% 
one = 1.0
one_third = 1.0/3.0
zero = one - one_third - one_third - one_third

print('one =', one, ' one_third =', one_third, ' zero =', zero)
#%% this is supposed to show how you cannot get to zero without real numbers and only floats
one = 1.0
one_tenth = 1.0/10.0
zero = one - one_tenth - one_tenth - one_tenth \
            - one_tenth - one_tenth - one_tenth \
            - one_tenth - one_tenth - one_tenth \
            - one_tenth

print('one =', one, ' one_tenth =', one_tenth, ' zero =', zero)
#%% this is to show the error message from dividing by zero
# get two integers from the user
dividend, divisor = eval(input('Please enter two numbers to divide: '))
# Divide them and report the result
print(dividend, '/', divisor, "=", dividend/divisor)
#%% have the user input a strin value, such as bobby
# Get a number from the user
value = eval(input('Please enter a number to cut in half: '))
# Report the result
print(value/2)
#%% this program performs a function which converts a temperature from degrees F to degrees C
# File tempconv.py
# Author: Rick Halterman
# Last modified: August 22, 2011
# Converts degrees Fahrenheit to degrees Celsius
# Based on the formula found at
# http://en.wikipedia.org/wiki/Conversion_of_units_of_temperature

# Prompt user for temperature to convert and read the supplied value
degreesF = eval(input('Enter the temperature in degrees F: '))
# Perform the conversion
degreesC = int(5/9*(degreesF - 32));
# Report the result
print(degreesF, 'degrees F =', degreesC, 'degrees C')
#%% File timeconv.py

# Get the number of seconds
seconds = eval(input("Please enter the number of seconds:"))
# First, compute the number of hours in the given number of seconds
# Note: integer division with possible truncation
hours = seconds // 3600 # 3600 seconds = 1 hours
# Compute the remaining seconds after the hours are accounted for
seconds = seconds % 3600
# Next, compute the number of minutes in the remaining number of seconds
minutes = seconds // 60 # 60 seconds = 1 minute
# Compute the remaining seconds after the minutes are accounted for
seconds = seconds % 60
# Report the results
print(hours, "hr,", minutes, "min,", seconds, "sec")
#%% File enhancedtimeconv.py
# Get the number of seconds
seconds = eval(input("Please enter the number of seconds:"))
# First, compute the number of hours in the given number of seconds
# Note: integer division with possible truncation
hours = seconds // 3600 # 3600 seconds = 1 hours
# Compute the remaining seconds after the hours are accounted for
seconds = seconds % 3600
# Next, compute the number of minutes in the remaining number of seconds
minutes = seconds // 60 # 60 seconds = 1 minute
# Compute the remaining seconds after the minutes are accounted for
seconds = seconds % 60
# Report the results
print(hours, ":", sep="", end="")
# Compute tens digit of minutes
tens = minutes // 10
# Compute ones digit of minutes
ones = minutes % 10
print(tens, ones, ":", sep="", end="")
# Compute tens digit of seconds
tens = seconds // 10
# Compute ones digit of seconds
ones = seconds % 10
print(tens, ones, sep ="")