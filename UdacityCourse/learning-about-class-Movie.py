# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 22:05:15 2017

@author: Felix
"""

import webbrowser

class Movie(): 
    '''When a Movie object is created, the Turtle method is called and able
    to get its movie trailer from an YouTube url''' # this is a class variable
    # instance methods
    def __init__(self, title, description, ratings, trailer):
        self.title = title
        self.description = description
        self.ratings = ratings
        self.trailer_url = trailer
        
    #create a function to pull the video for the movie trailer from youtube
        
    def get_trailer(self):
        webbrowser.open(self.trailer_url)
        
 #### 
        
# should always keep class in a different file #
# but for sake of simplicity lets just keep it here #
        
# first movie

toy_story = Movie('Toy Story', 'A cool movie about toys', '8/10', "http://www.youtube.com")
print(toy_story)