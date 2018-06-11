# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 10:15:10 2018

@author: dscabrego
"""
#%% Chapter 4
# Assign some Boolean variables
a = True
b = False
print('a =', a, ' b =', b)
# Reassign a
a = False;
print('a =', a, ' b =', b)
#%% File betterdivision.py

# Get two integers from the user
dividend, divisor = eval(input('Please enter two numbers to divide: '))
# If possible, divide them and report the result
if divisor != 0:
    print(dividend, '/', divisor, "=", dividend/divisor)
else:
    print('Ensure that the denominator is non-zero.')
#%% File betterdivision.py - ALTERNATIVE

# Get two integers from the user
dividend, divisor = eval(input('Please enter two numbers to divide: '))
# If possible, divide them and report the result
if divisor != 0: print(dividend, '/', divisor, "=", dividend/divisor)
else: print('Ensure that the denominator is non-zero.')
#%% Get two integers from the user
dividend, divisor = eval(input('Please enter two numbers to divide: '))
# If possible, divide them and report the result
if divisor != 0:
    quotient = dividend/divisor
    print(dividend, '/', divisor, "=", quotient)
print('Program finished')
#%%
# Request input from the user
num = eval(input("Please enter an integer in the range 0...9999: "))

# Attenuate the number if necessary
if num < 0: # Make sure number is not too small
    num = 0
if num > 9999: # Make sure number is not too big
    num = 9999

print(end="[") # Print left brace

# Extract and print thousands-place digit
digit = num//1000 # Determine the thousands-place digit
print(digit, end="") # Print the thousands-place digit
num %= 1000 # Discard thousands-place digit

# Extract and print hundreds-place digit
digit = num//100 # Determine the hundreds-place digit
print(digit, end="") # Print the hundreds-place digit
num %= 100 # Discard hundreds-place digit

# Extract and print tens-place digit
digit = num//10 # Determine the tens-place digit
print(digit, end="") # Print the tens-place digit
num %= 10 # Discard tens-place digit

# Remainder is the one-place digit
print(num, end="") # Print the ones-place digit

print("]") # Print right brace
#%% this program provides better feedback and indicates to the user not to divide by zero (0)
# Get two integers from the user
dividend, divisor = eval(input('Please enter two numbers to divide: '))
# If possible, divide them and report the result
if divisor != 0: print(dividend, '/', divisor, "=", dividend/divisor)
else: print('Division by zero is not allowed!')
#%%
d1 = 1.11 - 1.10
d2 = 2.11 - 2.10
print('d1 =', d1, ' d2 =', d2)
if d1 == d2: print('Same')
else: print('Different')
#%% Compound boolean expressions
value = eval(input("Please enter an integer value in the range 0...10: "))
if value >= 0:
    if value <= 10:
        print("In range")
print("Done")
#%%
value = eval(input("Please enter an integer value in the range 0...10: "))
if value >= 0 and value <= 10: # Only one, more complicated check
    print("In range")
print("Done")
#%% Enhanced nested loop
value = eval(input("Please enter an integer value in the range 0...10: "))
if value >= 0: # First check
    if value <= 10: # Second check
        print(value, "is in range")
    else:
        print(value, "is too large")
else:
    print(value, "is negative")
print("Done")