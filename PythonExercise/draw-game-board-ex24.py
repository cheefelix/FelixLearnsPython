# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 22:54:25 2017

@author: Felix
"""

#==============================================================================
# Draw A Game Board
# ex 24
# Ask the user what size game board they want to draw, 
# and draw it for them to the screen using Python’s print statement.
#==============================================================================

# step 1: write a function to draw the number of horizontal lines
# step 2: draw vertical lines

print(' --- --- --- ') 

print('|   |   |   |')

print(' --- --- --- ')

print('|   |   |   |')

print(' --- --- --- ')

print('|   |   |   |')

print(' --- --- --- ')



h = 3
w = 3 

horizontal  = (' --- ')
vertical    = ('|   |')

one_box = ( (horizontal*3) +'\n'+ '|' + ' '*3 + '|')
print(one_box)



# Draw A Game Board 

def draw_board( w, h ):
    horizontal = ' ---'
    vertical = '|   '
    vertical_right = '|'

    # first line
    print(horizontal * int(w))
    print(vertical * int(w) + vertical_right)

    # lines after first
    for i in range(h-1):
        print(horizontal * int(w))
        print(vertical * int(w) + vertical_right)

    print(horizontal * int(w))

    


draw_board(5,5)



print('\n-------another way using join----------------------\n')

a = '---'.join('    ')
b = '   '.join('||||')
print('\n'.join((a, b, a, b, a, b, a)))




########## not working ###########

def draw_box(number):
    horizontal  = (' --- ')
    vertical    = ('|   |')
    
    one_box = (horizontal+'\n'+vertical+'\n')   
    print( (one_box*number)+horizontal) 
  
draw_box(3)

########## not working ###########











