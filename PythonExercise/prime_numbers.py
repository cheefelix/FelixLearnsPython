# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 00:17:26 2017

@author: Felix
"""

# revision 
# checking if a number is prime

# 1. Given a number, return the divisors

num = int( input('Number: ') )

def divisor(num):
    divisor = []
    
    if num > 0:
        for i in range (1, num+1):
            if num % i == 0:
                divisor.append(i)   
    else:
        print('please insert positive number')
    return divisor
            
divisor(num)



# 2. if a number is prime; divisor will only have 2 items.

# definition of prime:  if it has exactly two positive divisors, 1 and the number itself
# 1 is not a prime number cause it;s only divisor is itself. 

number = int( input('Prime or not?: '))

def check_prime(number):
    
    divisor_list = divisor(number)
    if number == 1:
        return ('{} is not a prime number!'.format(number)) 
    if number > 1:
        if len(divisor_list) <= 2:
            return ('{} is a prime number'.format(number))
        else:
            return ('{} is not a prime number!'.format(number))

check_prime(number)
    