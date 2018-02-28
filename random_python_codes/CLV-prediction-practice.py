# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 19:45:29 2018

@author: Felix

https://github.com/datascienceinc/oreilly-intro-to-predictive-clv/blob/master/oreilly-an-intro-to-predictive-clv-tutorial.ipynb

"""

import pandas as pd

link = 'https://raw.githubusercontent.com/datascienceinc/oreilly-intro-to-predictive-clv/master/cdnow_transaction_log.csv'
data = pd.read_csv(link)


data.head()