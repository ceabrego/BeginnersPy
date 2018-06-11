# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 08:25:19 2018

@author: dscabrego
"""
#%% using input
print('Please enter some text:')
x = input() #this command waits for an input from the user on the command prompt
print('Text entered:', x) #this line shows what text was entered for variable x
print('Type:', type(x))
#%%
print('Please enter an integer value:')
x = input() #this accepts input information from the user command prompt and is used for the value of x
print('Please enter another integer value:')
y = input() #this accepts input information from the user command prompt and is used for the value of y
#note that the values that were used stored for x and y as string values
num1 = int(x)
num2 = int(y)
print(num1, '+', num2, '=', num1 + num2)
#%% inputing values and storing them
x = input('Please enter an integer value: ')
y = input('Please enter another integer value: ')
num1 = int(x)
num2 = int(y)
print(num1, '+', num2, '=', num1 + num2)
#%% this is the shortest version of the last 3 cells
num1 = int(input('Please enter an integer value: '))#here you convert the input into an integer in one step
num2 = int(input('Please enter another integer value: '))#here you convert the input into an integer in one step
print(num1, '+', num2, '=', num1 + num2)
#%% this cell looks to find how to evaluate what the input value is
x1 = eval(input('Entry x1? '))
print('x1 =', x1, ' type:', type(x1))

x2 = eval(input('Entry x2? '))
print('x2 =', x2, ' type:', type(x2))

x3 = eval(input('Entry x3? '))
print('x3 =', x3, ' type:', type(x3))

x4 = eval(input('Entry x4? '))
print('x4 =', x4, ' type:', type(x4))

x5 = eval(input('Entry x5? '))
print('x5 =', x5, ' type:', type(x5))
#%% this cell puts multiple values from one line
num1, num2 = eval(input('Please enter number 1, number 2: '))#the input needs to go in as 'x, y'
print(num1, '+', num2, '=', num1 + num2)
#%% entering arithmatic
print(eval(input()))
#%% Section 2.8 - Controlling the print Function, the best way to describe this is to go ahead and execute this code
print('A', end='')
print('B', end='')
print('C', end='')#this will end up executing ABC
print()
print('X')
print('Y')
print('Z')#this will end up executing X new line, Y new line Z new line. The print statement essentially adds a new line
#%% print separation
w, x, y, z = 10, 15, 20, 25
print(w, x, y, z)
print(w, x, y, z, sep=',')#the sep function separates the values with whatever argument there is in quotations
print(w, x, y, z, sep='')
print(w, x, y, z, sep=':')
print(w, x, y, z, sep='-----')
#%%
print(' x \n','y \n','z \n')