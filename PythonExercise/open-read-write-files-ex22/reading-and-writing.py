# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 23:28:48 2017

@author: Felix
"""

#==============================================================================
# http://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html
# # Ex 22
# # Practicing reading and writing new files
# concepts: open(), split(), dictionary = {}, 
#==============================================================================

# # with open("felix-learns-how-to-open-file.txt", "w") as w:
# # w.write('hello world\nthis is felix\nim not good at this yet\n but i will be')


# reading the above writen file   

dictionary_count = {}
with open("felix-learns-how-to-open-file.txt", "r") as r:
    
    for line in r:
        line = line.strip() 
        
        if line in dictionary_count:
            dictionary_count[line] += 1
            
        else:
            dictionary_count[line] = 1
        
print(dictionary_count)

r.close()


#==============================================================================
# # count how many of each “category” of each image there are
#==============================================================================

# reading sun.txt 
dictionary_count = {}
with open('sun.txt', 'r') as read_file:
    for line in read_file:        
        print(line)
        
        line = line.strip()
        
        line = line.split('/') 
        line = line[2]
        
        if line in dictionary_count:
            dictionary_count[line] += 1
        else:
            dictionary_count[line] = 1

print(dictionary_count)

read_file.close()

# another way of doing it;  but i dont understand the -26

counter_dict = {}
with open('sun.txt') as f:
	line = f.readline()
	while line:
		line = line[3:-26]
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print(counter_dict)

f.close()







