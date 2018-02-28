# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 21:15:30 2017

@author: Felix
"""

import time
import webbrowser

url = "http://www.youtube.com"
total_break = 2
break_count = 0

print("This was run on " + time.ctime() ) # time.ctime() prints the current time date 

while (total_break > break_count):
    time.sleep(10)
    webbrowser.open(url)    
    break_count += 1 




