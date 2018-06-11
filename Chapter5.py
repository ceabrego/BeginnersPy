# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:04:12 2018

@author: dscabrego
"""
# Chapter 5 - Iterations
#%%
print(1)
print(2)
print(3)
print(4)
print(5)
#%% alternative method for printing with a for loop
count = 1
for i in range(5):
    print(count)
    count +=1
#%% Alternative method for printing in a while loop
count = 1
while count<=5:
    print(count)
    count+=1
#%%
entry = 0
summ = 0

print('Enter numbers to sum, end with a negative number: ')
while entry >=0:
    entry = eval(input())
    if entry >=0:
        summ += entry        
print(summ)
#%% definite1
n=1
while n <=10:
    print(n)
    n+=1
#%%
n=1
stop = int(input('Give a positive stopping integer '))
while n <= stop:
    print(n)
    n += 1
    
#%% using the for statement
for n in range(1,12,2): #note that n goes from the first to the second argument in steps of the last argument
    print(n)
#%% using the for statement in reverse
for n in range(21,0,-3):
    print(n,'',end='')
#%%
# Print a multiplication table to 10 x 10
# Print column heading
print(" 1  2  3  4  5  6  7  8  9  10")
print(" +----------------------------------------")
for row in range(1, 11): # 1 <= row <= 10, table has 10 rows
    if row < 10: # Need to add space?
        print(" ", end="")
        print(row, "| ", end="") # Print heading for this row.
        for column in range(1, 11): # Table has 10 columns.
            product = row*column; # Compute product
            if product < 100: # Need to add space?
                print(end=" ")
            if product < 10: # Need to add another space?
                print(end=" ")
            print(product, end=" ") # Display product
        print()
#%%
MAX = 18

# First, print heading
print(end=" ")
# Print column heading numbers
for column in range(1, MAX + 1):
    print(end=" %2i " % column)
print() # Go down to the next line

# Print line separator; a portion for each column
print(end=" +")
for column in range(1, MAX + 1):
    print(end="----") # Print portion of line
print() # Go down to the next line

# Print table contents
for row in range(1, MAX + 1): # 1 <= row <= MAX, table has MAX rows
    print(end="%2i | " % row) # Print heading for this row.
    for column in range(1, MAX + 1): # Table has 10 columns.
        product = row*column; # Compute product
        print(end="%3i " % product) # Display product
    print() # Move cursor to next row
#%% File permuteabc.py
# The first letter varies from A to C
for x in 'DEF':
    for y in 'DEF': # The second varies from A to C
        if y != x: # No duplicate letters allowed
            for z in 'DEF': # The third varies from A to C
# Don't duplicate first or second letter
                if z != x and z != y:
                    print(x + y + z)
#%%
count=0
for w in 'QRST':
    for x in 'QRST':
        if x!=w:
            for y in 'QRST':
                if y!=x and y!=w:
                    for z in 'QRST':
                        if z!=x and z!=y and z!=w:
                            print(w + x + y + z)
                            count+=1
print('There are',count, 'patterns')
                    
                