# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 19:08:30 2017

@author: Felix
"""


import numpy as np
import pandas as pd

# read files
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
    
chipo = pd.read_csv(url, sep = '\t')

# check column names
chipo.columns

# group and sum 
c = chipo.groupby('item_name')
c = c.sum()

# sort
c = c.sort_values(['quantity'], ascending=False)
c.head(1) 

## finding for choice_description

d = chipo.groupby('choice_description').sum()
d = d.sort_values( ['quantity'], ascending=False)
# or    d = d.quantity.sort_values(ascending=False)
d.head(1)

# how many items were order in total ?
d.quantity.sum()


# how many orders were made in the period
chipo.order_id.value_counts().count()

#   n.b. value_counts:
#   Returns object containing counts of unique values.

# average order per month

a = chipo.groupby(['order_id']).sum()

a.quantity.sum()/a.quantity.sum()

a.quantity.sum()

a.quantity.count()

chipo.groupby(by=['order_id']).sum().mean()['item_price']


order_grouped = chipo.groupby(by=['order_id']).sum()
order_grouped.mean()['item_price']


# How many items sold
chipo.item_name.value_counts().count()


#==============================================================================
# how many products are more than $10
#==============================================================================

chipo.head(10)
chipo.info()

# convert item_price column to float

prices = []
for i in chipo.item_price: 
    prices.append( float(i[1:-1]) )
    
chipo.item_price = prices     # update the column

# or    
# prices = [float(value[1 : -1]) for value in chipo.item_price]


# make the comparison
# into a dataFrame
chipo10 = chipo [ chipo.item_price > 10.00 ]

# into a list
#chipo10 = []
#for i in chipo.item_price:
#    if i > 10:
#        chipo10.append(i)

chipo10.head()

len(chipo10)
    
#==============================================================================
# What is the price of each item?
# print a data frame with only two columns item_name and item_price   
#==============================================================================
    

chipo.head(10)

two_columns = chipo.drop_duplicates(['item_name','quantity'])  # this is how you drop duplicates

two_columns = two_columns[two_columns.quantity == 1]               # this is how u filter

two_columns = two_columns[['item_name', 'item_price']]              # this is how to select two columns

two_columns = two_columns.sort_values(by = "item_price", ascending = False)


#==============================================================================
# sort by name
#==============================================================================

two_columns = two_columns.sort_values(by = 'item_name', ascending = True)


#==============================================================================
# Step 7. What was the quantity of the most expensive item ordered?
#==============================================================================
expensive = chipo.sort_values(by = "item_price", ascending = False)
expensive.head(1)

# or
# chipo.sort_values(by = "item_price", ascending = False).head(1)


#==============================================================================
# How many times were a Veggie Salad Bowl ordered
#==============================================================================

veggie = chipo[ chipo.item_name == 'Veggie Salad Bowl' ]  
len(veggie) # you can check len of dataFrames (number of rows)


#==============================================================================
# How many times people order more than one Canned Soda
#==============================================================================

chipo.head(10)

soda = chipo[ (chipo.item_name == 'Canned Soda') & ( chipo.quantity > 1 )]
len(soda)


#==============================================================================
# to remember

# use iloc to filter columns. 
## eg. euro12.iloc[:, 0:-3]
## always use iloc - iloc  is integer based.

# use isin to find more than one names etc.
## eg. euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']]

# use startwith to find first letter.
## eg. euro12[euro12.Team.str.startswith('G')]
#==============================================================================


#==============================================================================
#  apply 
#==============================================================================

# create a function to capitalise strings
def cap(string):
    string = string.upper()
    return string
    
# apply it to cap stuff # only works on pandas dataFrame
chipo.item_name.apply(cap)


#==============================================================================
# convert to date time - pd.to_datetime

#==============================================================================

pd.to_datetime(crime)
crime.Year = pd.to_datetime(crime.Year, format='%Y')
crime.info()


#==============================================================================
#  better way to set index - set_index
#==============================================================================
 
crime = crime.set_index('Year', drop = True)
crime.head()
 
 
#==============================================================================
#  The best way to do this in pandas is to use drop:
#==============================================================================
 
df = df.drop('column_name', 1)

#where 1 is the axis number (0 for rows and 1 for columns.)
#To delete the column without having to reassign df you can do:


#==============================================================================
# idxmax(0)

# this is magic
# Return index of first occurrence of maximum over requested axis. NA/null values are excluded.
#==============================================================================

