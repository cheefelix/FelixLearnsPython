## ex 12

# Write a program that takes a list of numbers
# (for example, a = [5, 10, 15, 20, 25]) and
# makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

'''
a = [5, 10, 15, 20, 25]

 
def list_in_list(a):
    b = []
    b.append(a[0])
    b.append(a[-1])
    return (b)


def list_ends(a_list):
    return [a_list[0], a_list[len(a_list)-1]]

'''

## ex 13

# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions. Make sure to ask the user to enter
# the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where
# the next number in the sequence is the sum of the previous two numbers in the sequence.

'''
length = int ( input('Numbers of Fibonnaci numbers: ') )

def fibo_num( length ):
    a = [0,1]
    if length == 1:
        print ([a[0]])
    elif length == 2:
        print (a)
    elif length > 2:
        for i in range(0, length):
            b = a[i] + a[i+1]
            a.append(b)
        print (a[:length])
    else:
        print ('Please insert a positive number higher than 0')
        
fibo_num( length )
'''

## ex 14
# Write a program (function!) that takes a list and returns a new list
# that contains all the elements of the first list minus all the duplicates.

# concept; using sets() to remove duplicates and list() to convert back to a list

'''
a = [9,10,11,12,13,15,2,2,2,2]
b = [1,0,7,6,5,4]


#a_new_set = set(a) # converting a list to a set. will contain only unqiue values
#back_to_list = list(a_new_set) # convert back to a list with unqiue values now


# using loops
print('using loops')

num =[]
for i in a:
    if i not in num and i in a:
        num.append(i)
print ( num )

# using list comprehenstion
print ('using list comprehenstion')
num = list( set([ i for i in a ]) )
print (num)


# using list()
print('using list()')

def no_duplicates_list(a):

    print ( '{} is a list with duplicates'.format(a) ) 
    
    unique = list( set(a) )
    print ('{} is a list without duplicates!'.format(unique))


no_duplicates_list(a)
'''




## ex 15

# Write a program (using functions!) that asks the user for a long
# string containing multiple words. Print back to the user the same
# string, except with the words in backwards order.
# For example, say I type the string:

# concept; split() and join()
'''
w = 'Hello who are you'
print('{}\n'.format(w))

print('Normal function: ')
def reverse_words_order(w):

    split_words = w.split(' ')

    reverse_words_in_list = split_words[::-1]

    reverse_string = " ".join(reverse_words_in_list)

    print(reverse_string)

reverse_words_order(w)


print ('\nIn one line: ')

def reverseWord(w):
    print( ' '.join(w.split()[::-1]) )

reverseWord(w)
'''


## ex 16

#Write a password generator in Python.
# Be creative with how you generate passwords -
# strong passwords have a mix of lowercase letters, uppercase letters,
# numbers, and symbols. The passwords should be random, generating a new password
# every time the user asks for a new password.
#Include your run-time code in a main method.
'''
import random
import string


symbols = string.punctuation
numbers = [0,1,2,3,4,5,6,7,8,9]
alpha_lower =  string.ascii_lowercase
alpha_upper =  string.ascii_uppercase

# below; does not work -- 
length = int( input('What is the length you want for your password?: ') )

password=''
while len(password) < length:
    
    random_one_to_four = random.randint(1,4)  # randomly choose between symbols, numbers, uppercase, lowercase
    
    if random_one_to_four == 1:
        password += random.sample(symbols,1)
        
    elif random_one_to_four == 2:
        password += random.sample(numbers,1)
        
    elif random_one_to_four == 3:
        password += random.sample(alpha_lower,1)
        
    else:
        password += random.sample(alpha_upper,1)

print(password)



## USE random.sample() ; MAKES LIFE EASIER FOR YOU!!

# generate a password with length "passlen" with no duplicate characters in the password

#s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
s = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + '0123456789'
passlen = 8
p =  "".join(random.sample(s,passlen ))
print (p)

'''



## ex 17

#Use the BeautifulSoup and requests Python packages to
# print out a list of all the article titles on the New York Times homepage.

import urllib.request

url = 'http://github.com'
r = urllib.requests.get(url)
r_html = r.text













                                                                                                                                                                                                                                                         
