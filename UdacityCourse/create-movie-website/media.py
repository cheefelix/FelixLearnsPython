# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 20:38:46 2017

@author: Felix
"""

import webbrowser

class Movie():
    
    # init is the constructor # self is calling itself
    def __init__(self, movie_title, storyline, poster_image, trailer):
        
        # this are the intance / object variables
        self.title = movie_title 
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
        
    def show_trailer(self): # this is the intance / object methods
        webbrowser.open(self.trailer_youtube_url)