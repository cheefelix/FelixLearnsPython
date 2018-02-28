# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 20:36:34 2017

@author: Felix
"""


## ex 6

# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

'''
while 1==1:
    a = input('Please input a string :')
    
    for i in a:
        b = a[::-1]
        
    if a == 'quit':
        break
    elif a == b and len(a)>1:
        print('{} is a palindrome!'.format(a))
    else:
        print('{} is not a palindrome'.format(a))
'''
  
# alula
# up to new era.

# step 1: count the number of characters
# step 2: print a reverse version of it
# step 3: match it with the input
# step 4: if match, print it is a palindrome


## ex 7

# Let’s say I give you a list saved in a variable: 
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
# Write one line of Python that takes this list a and makes a new 
# list that has only the even elements of this list in it.
'''
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# normal way first
b = []

for i in a:
    if i % 2 == 0:
        b.append(i)
    else:
        None

# in one line
b = [number for number in a if number % 2 == 0]
print(b)

'''



## ex 8
# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), 
# compare them, print out a message of congratulations to 
# the winner, and ask if the players want to start a new game)

#Remember the rules:

#Rock beats scissors
#Scissors beats paper
#Paper beats rock

###### example while loop code #####
'''
quit = input('Type "enter" to quit:' )

while quit != "enter":
    quit = input('Type "enter" to quit:' )




 while True: 
    usr_command = input("Enter your command: ")
    if usr_command == "quit":
      break
    else: 
      print("You typed " + usr_command)

#####

print("Please pick one:",
            "rock, scissors, paper")

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_a = str(input("Player a: "))
    player_b = str(input("Player b: "))
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b

    if dif in [-1, 2]:
        print('player a wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print('player b wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print('Draw.Please continue.')
        print('')


'''



## ex 9

# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, 
# then tell them whether they guessed too low, too high, or exactly right.

'''
import random

random_number = random.randint(1,9) 
guess = 0
while True:
    number =( input('Please insert any number from 1 to 9: ') )
    guess += 1
    if number == 'exit':
        break      
    if random_number == int(number):
        print('You guessed correct!')    
        print('You have guessed {} times!'.format(guess))
        break
    elif random_number >  int(number):
        print('You guessed too low')
        continue
    elif random_number <  int(number):
        print('You guessed too high')
        continue
'''

## ex 10

#Take two lists, say for example these two:
#and write a program that returns a list that contains only the elements that 
# are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes
'''
import random 

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# randomly generated lists

a = [] 
for i in range(1, random.randint(1,9)):
    a.append( random.randint(1,9) )


b = [] 
for i in range(1, random.randint(1,9)):
    b.append( random.randint(1,9) )

# print similar numbers from list a and b
numbers = []
for i in a:
    for j in b:
        if i == j and i not in numbers:
            numbers.append(i)

print(numbers)


# in one line

a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
result = [i for i in set(a) if i in b]
print(result)


# while loop

a=[]
b=[]
numbers=[]
count = 0
while True:
    count += 1
    for i in range(1, random.randint(1,9)):
        a.append( random.randint(1,1000) )
    for i in range(1, random.randint(1,9)):
        b.append( random.randint(1,1000) )
    
    for i in a:
        for j in b:
            if i == j and i not in numbers:
                numbers.append(i)

    print(numbers)
    print('loop {} times'.format(count))
    if len(numbers) > 10 :
        break
    else:
        continue




## ex 20

#Write a function that takes an ordered list of numbers 
#(a list where the elements are in order from smallest to largest) 
#and another number. The function decides whether or not 
#the given number is inside the list and returns (then prints) an appropriate boolean.

# using a funcion
def find(ordered_list, element_to_find):
  for element in ordered_list:
    if element == element_to_find:
      return True
  return False
    
    
 # no function   
import random
a = ( random.sample(range(10), k=5) )
a.sort()


b = 5
for i in a:
    if i == b:
        output = True
    else:
        None
        
print(output)

'''

# using binary search

number = 50
ordered_list = [1,5,7,8,9,11,55]

def binary_search(ordered_list, number):    
    
    # if list have 1 item
    if len(ordered_list) == 1:
        return True if ordered_list[0] == number else False # new concept here
        
    # find the middle index
    middle_index = int ( len(ordered_list) / 2)
    
    #check if middle number is the number we r looking for
    if ordered_list[middle_index] == number:
        return True 
            
    #if the value in the middle of list is larger than number    
    elif ordered_list[middle_index] > number:
        return binary_search( ordered_list[:middle_index:], number )
    
    #if the value in the middle of list is smaller than number
    else:
        return binary_search( ordered_list[middle_index::], number )

binary_search(ordered_list, number)                  
        
# note to self: USE THE RETURN STATEMENT WHEN WRITING IF STATEMENTS
# The point of functions in general is to take in inputs and return something. 
# The return statement is used when a function is ready to return a value to its caller.
# return causes the function to stop executing and hand a value back to whatever called it.


    
    
