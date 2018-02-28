# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:51:10 2017

@author: Felix
"""

#==============================================================================
# geting all of Hacker News front page title and put into a text file, 
# then count the frequency of words in it
#==============================================================================

import requests
from bs4 import BeautifulSoup
import operator 

html = 'https://news.ycombinator.com/news'


r = requests.get(html)  #     get 
text = r.text           # convert to string

soup = BeautifulSoup(text, 'html.parser') # convert to a soup # give hierachy 

print( soup.prettify() )


# finding the title
title = soup.find_all(class_="storylink")


# add all title into a list 
a_list = []
for t in title:
    a_list.append(t.contents[0].strip())


# creating a empty text file #w = write 
hn_text = open('hn.txt', 'w')    

# write the list into the file and adding a line after each title: \n    
hn_text.write( '\n'.join(a_list) )
                
# best practice; close open file to clear memory space                
hn_text.close()



#==============================================================================
# Count the number of repeat words in the titles
#==============================================================================

# first read the text file we created

text_file = open('hn.txt', 'r')

dict_count = {}
word_list = []

# make a list of words in the text file 
for line in text_file:
    line = line.strip()      
    word_list = word_list + line.split(' ')

text_file.close()   
 
 
# creating a dictionary that show how many times a word is repeated
for word in word_list:
    if word in dict_count:
        dict_count[word] += 1
    else:
        dict_count[word] = 1
    

# sort by dictionary key values
sorted_x = sorted(dict_count.items(), key=operator.itemgetter(1))


            
            