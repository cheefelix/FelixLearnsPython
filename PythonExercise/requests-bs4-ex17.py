# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 22:49:57 2017

@author: Felix
"""

#==============================================================================
# ex 17 
# Decode A Web Page
# Use the BeautifulSoup and requests Python packages to 
# print out a list of all the article titles on the New York Times homepage.
#==============================================================================


from bs4 import BeautifulSoup 
import requests


url = 'https://www.nytimes.com/'
r = requests.get(url)

r_html = r.text         # step 1: to get the HTML of the page as a string. 

# step 2: using BeautifulSoup to 
# To solve our problem of parsing
# (reading, understanding, interpreting) the string of HTML 

soup = BeautifulSoup(r_html, 'html.parser')
print(soup.prettify()) # here; we can see the hierarchy of the HTML code of the website


title = soup.find_all(class_="story-heading")

# find and loop through all elements on the page with the 
# class name "story-heading"
for story_heading in title: 
    # for the story headings that are links, print out the text
    # and format it nicely
    # for the others, take the contents out and format it nicely
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip()) # strip() remove empty spaces
    else: 
        print(story_heading.contents[0].strip())
        
        
#==============================================================================
# ex 19
# Using the requests and BeautifulSoup Python libraries, print to the screen the 
# full text of the article on this website: 
# http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
# The article is long, so it is split up between 4 pages. Your task is to print 
# out the text to the screen so that you can read the full article without having 
# to click any buttons.       
#==============================================================================


        
        
        