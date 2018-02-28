# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 21:53:41 2017

@author: Felix
"""

# a problem here
# can't check for sentences

import urllib

def read_text():    
    quotes = open("/Users/Felix/Desktop/random_wiki_text.txt")      
    contents = quotes.read()   
    print(contents)   
    quotes.close()
    
    check_curse_words(contents)
    
    
#some_text = 'aaa'

def check_curse_words(some_text):
    
    connections = urllib.request.urlopen('http://www.wdylike.appspot.com/?q='+some_text)       
    output = connections.read()    
    print(output)    
    connections.close()
 

#check_curse_words(some_text)

read_text()   