# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 22:31:38 2017

@author: Felix
"""

import media
import fresh_tomatoes

### object 1
### toy_story is an object
toy_story = media.Movie("Toy Story",
                         "Toy Story is a 1995 American computer-animated buddy comedy adventure film produced by Pixar Animation Studios for Walt Disney Pictures",
                         "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=1guCjulfnZI")
                         
print(toy_story.storyline)
toy_story.show_trailer()



### object 2
avatar = media.Movie("Avatar",
                         "The film is set in the mid-22nd century, when humans are colonizing Pandora, a lush habitable moon of a gas giant in the Alpha Centauri star system, in order to mine the mineral unobtanium,[9][10] a room-temperature superconductor.[11] ",
                         "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                         "https://www.youtube.com/watch?v=5PSNL1qE6VY")
                         
print(avatar.storyline) # using the object variable
avatar.show_trailer() # using the object methods



movies = []
movies = [toy_story, avatar]

fresh_tomatoes.open_movies_page(movies)