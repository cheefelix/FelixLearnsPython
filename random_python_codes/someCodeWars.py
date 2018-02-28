# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 22:03:30 2017

@author: Felix
"""


people = [25, 25, 50]

people = [25, 100]

people = [100, 50, 25]

people = [25, 50, 100]

def tickets(people):
    
    for i in range(0, len(people)):
        
        if people[i] > 25:
            return 'NO'
        else:
            return 'YES'
            
        if people[i] - people[i+1] == 0:
            return 'YES'
        elif people[i] - people[i+1] == -25:
            return 'YES'
        else:
            return 'NO'

tickets(people)     

'''
def tickets(people):
    
    if people[0] == 25 and people[1] == 25:
        return 'YES'
    elif people[0] == 25 and people[1] == 50:
        return 'YES'
    else:
        return 'NO'      

tickets(people)       
'''