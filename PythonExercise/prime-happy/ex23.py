# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 22:22:03 2017

@author: Felix
"""

#==============================================================================
# Exercise 23
# Given two .txt files that have lists of numbers in them, 
# find the numbers that are overlapping. One .txt file has 
# a list of all prime numbers under 1000, 
# and the other .txt file has a list of happy numbers up to 1000.
#==============================================================================


# 1. read both files

prime_numbers = []
with open('prime-num.txt', 'r') as prime:
    line = prime.readline()
    while line:
        prime_numbers.append(int(line))  # this is magical. if int('1\n'); it just prints out 1 
        line = prime.readline()
        
        
happy_numbers = []    
with open('happy-num.txt', 'r') as happy:
    line = happy.readline()
    while line:
        happy_numbers.append(int(line))
        line = happy.readline()
   
         
match = [ num for num in prime_numbers if num in happy_numbers]            
print(match)



## better way; making a function first then match the two list 

def filetolistofints(filename):
	list_to_return = []
	with open(filename) as f:
		line = f.readline()
		while line:
			list_to_return.append(int(line))
			line = f.readline()
	return list_to_return

primeslist = filetolistofints('prime-num.txt')
happieslist = filetolistofints('happy-num.txt')

overlaplist = [elem for elem in primeslist if elem in happieslist]
print(overlaplist)