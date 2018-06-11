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
#%%
print("Help! My computer doesn't work!")
print("Does the computer make any sounds (fans, etc.)")
choice = input("or show any lights? (y/n):")
# The troubleshooting control logic
if choice == 'n': # The computer does not have power
    choice = input("Is it plugged in? (y/n):")
    if choice == 'n': # It is not plugged in, plug it in
        print("Plug it in. If the problem persists, ")
        print("please run this program again.")
    else: # It is plugged in
        choice = input("Is the switch in the \"on\" position? (y/n):")
        if choice == 'n': # The switch is off, turn it on!
            print("Turn it on. If the problem persists, ")
            print("please run this program again.")
        else: # The switch is on
            choice = input("Does the computer have a fuse? (y/n):")
            if choice == 'n': # No fuse
                choice = input("Is the outlet OK? (y/n):")
                if choice == 'n': # Fix outlet
                    print("Check the outlet's circuit ")
                    print("breaker or fuse. Move to a")
                    print("new outlet, if necessary. ")
                    print("If the problem persists, ")
                    print("please run this program again.")
                else: # Beats me!
                    print("Please consult a service technician.")
            else: # Check fuse
                print("Check the fuse. Replace if ")
                print("necessary. If the problem ")
                print("persists, then ")
                print("please run this program again.")
else: # The computer has power
    print("Please consult a service technician.")
#%%
value = eval(input("Please enter an integer in the range 0...5: "))
if value < 0:
    print("Too small")
else:
    if value == 0:
        print("zero")
    else:
        if value == 1:
            print("one")
        else:
                if value == 2:
                    print("two")
                else:
                        if value == 3:
                            print("three")
                        else:
                                if value == 4:
                                    print("four")
                                else:
                                        if value == 5:
                                            print("five")
                                        else:
                                            print("Too large")
print("Done")
#%%
value = eval(input("Please enter an integer in the range 0...5: "))
if value < 0:
    print("Too small")
elif value == 0:
    print("zero")
elif value == 1:
    print("one")
elif value == 2:
    print("two")
elif value == 3:
    print("three")
elif value == 4:
    print("four")
elif value == 5:
    print("five")
else:
    print("Too large")
print("Done")
#%% Date transformer
month = eval(input('Enter a month value (1-12)'))
day = eval(input('Enter a day of the month'))
if month == 1:
    print('January', end='')
elif month == 2:
    print('February',end='')
elif month == 3:
    print('March',end='')
elif month == 4:
    print('April',end='')
elif month == 5:
    print('May',end='')
elif month == 6:
    print('June',end='')
elif month == 7:
    print('July',end='')
elif month == 8:
    print('August', end='')
elif month ==9:
    print('September',end='')
elif month == 10:
    print('October',end='')
elif month == 11:
    print('November',end='')
else:
    print('December',end='')
    
print(' the', day)
#%% safe divider
# Get the dividend and divisor from the user
dividend, divisor = eval(input('Enter dividend, divisor: '))
# We want to divide only if divisor is not zero; otherwise,
# we will print an error message
if divisor != 0:
    print(dividend/divisor)
else:
    print('Error, cannot divide by zero')
#%%
dividend, divisor = eval(input('Enter a numerator, denominator '))
print(dividend/divisor) if divisor != 0 else print('Cannot divide by zero!')
#%%
n = eval(input('Enter a number to find the absolute: '))
print(' |',n,'| = ', (-n if n < 0 else n))