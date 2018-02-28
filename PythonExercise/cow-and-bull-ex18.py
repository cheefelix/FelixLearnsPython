
## ex 18

'''
Randomly generate a 4-digit number.
Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place,
they have a “cow”. For every digit the user guessed correctly in the
wrong place is a “bull.” Every time the user makes a guess,
tell them how many “cows” and “bulls” they have.
Once the user guesses the correct number, the game is over.
Keep track of the number of guesses the user makes throughout teh game
and tell the user at the end.
'''


import random

# Generate 4 random digits
random_num = ''
count = 1
while count < 5: 
    random_num += str(random.randint(1,9))
    int(random_num)
    count += 1
    
random.randint(1,9)
print(random_num)


# cows and bulls

counter_1 = 0
counter_2 = 0
guesses = 0

while True:
    user_number =  ( input (' Please insert 4 numbers: ') )
    if user_number == 'exit':
        break
    
    for i in range(0,4):
        if user_number[i] == random_num[i]:  
            counter_2 += 1
        else:
            counter_1 += 1
            
    guesses += 1
    print ( str(counter_1) + ' ' + 'cow' , str(counter_2) + ' ' + 'bull' )
    
    if counter_1 == 4:
            user_number = 'exit'
            print("You win the game after " + str(guesses) + "! The number was "+str(random_num))
            break #redundant exit

    else:          
            print("Your guess isn't quite right, try again.")
            counter_1 = 0
            counter_2 = 0




