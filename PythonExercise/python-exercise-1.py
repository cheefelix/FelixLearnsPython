
### http://www.practicepython.org/

## Ex 1
#   Create a program that asks the user to enter their name and their age.
#   Print out a message addressed to them that tells them the year that
#   they will turn 100 years old.
'''
import time
from time import gmtime, strftime

name = input('name : ')
age  = input('age : ')

age2 = (100 - int(age))

print((name) + ', ' + age + ' ' + '\n' + 'You will turn 100 y.o in {} years'.format( age2 ) )
print ('You will turn {} in the year: '.format(100), int( time.strftime("%Y")) + age2 ) 
'''

## Ex 2
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# extra:    If the number is a multiple of 4, print out a different message.
# extra:    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#           If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''
number = int ( input('Number : ') )
check = int ( input('Checking : ') )

if number % 4 == 0:
    print ('{} is divisable by 4!'.format(number))
    
elif number % 2 == 0:
    print ('{} is an even number'.format(number) )

else:
    print ('{} is not an even number'.format(number) )


if number % check == 0:
    print (str(number) + ' is divisable by ' + str(check) )
else:
    print ('What? Number/Check is odd, like you.')
'''


## Ex 3
# Take a list, say for example this one:   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# extra 1:
# Instead of printing the elements one by one,
# make a new list that has all the elements less than 5 from this list in it and print out this new list.

# extra 2:
# Write this in one line of Python.

# extra 3:
# Ask the user for a number and return a list that contains only elements from the original
# list a that are smaller than that number given by the user.
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

number = int ( input ('Print a list of number less than : ') )


b = []
for i in a:
    if i < number:
        b = b + [i]

print (b)


# in one line
print( list(filter(lambda x:x < number, a) ) )
'''

## Ex 4
# Create a program that asks the user for a number and then prints out a
# list of all the divisors of that number. (If you don’t know what a divisor is,
# it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''
number = int ( input('Number : ') )

a = []

for i in range (1, number + 1):
    if number % i == 0 and number >= 0:
        a.append(i)                    
print ( a )
'''


## Ex 5
'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
'''

# extra
# Randomly generate two lists to test this
'''
import random

a = []
for aa in range(1,10):
    a.append((random.randint(1, 10)))

b = []
for bb in range(1,10):
    b.append((random.randint(1, 10)))

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

num = []

for i in a:
    for j in b:
        if i == j and (i not in num):
            num.append(i)
            
print(num)           
'''

## Ex 6

































