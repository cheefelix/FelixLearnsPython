# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 14:49:56 2018

@author: f

https://www.kaggle.com/dansbecker/your-first-scikit-learn-model

"""

import pandas as pd
import numpy as np


# =============================================================================
# explore data
# =============================================================================
mel_data = pd.read_csv('melb_data.csv')

mel_data.head(10)


mel_data.info()
mel_data.columns
mel_data.Price.head(10)

two_col = ['Price', 'Distance']
mel_data[two_col].describe()

# drop nan
mel_data = mel_data.dropna(axis=0)

# =============================================================================
# model
# =============================================================================

# choosing prediction target

y = mel_data.Price

# choosing predictors

mel_data.columns
mel_predictors = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude' ]

X = mel_data[mel_predictors]


# model building

    # Define: What type of model will it be? A decision tree? Some other type of model? Some other parameters of the model type are specified too.
    # Fit: Capture patterns from provided data. This is the heart of modeling.
    # Predict: Just what it sounds like
    # Evaluate: Determine how accurate the model's predictions are.

from sklearn.tree import DecisionTreeRegressor


# define model
mel_model = DecisionTreeRegressor()

# fot model
mel_model.fit(X, y)  # the output describes some parameters about the type of model you've built. Don't worry about it for now.


print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(mel_model.predict(X.head()))


# =============================================================================
# model validation
# =============================================================================

from sklearn.metrics import mean_absolute_error

pred_home_price = mel_model.predict(X)
mean_absolute_error(y, pred_home_price) # "in-sample" score 

# in sample data can be bad and bias
# using validation data.

from sklearn.model_selection import train_test_split

    # split data into training and validation data, for both predictors and target
    # The split is based on a random number generator. Supplying a numeric value to
    # the random_state argument guarantees we get the same split every time we
    # run this script.
    
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

# Define model
mel_model = DecisionTreeRegressor()

# Fit model
mel_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = mel_model.predict(val_X)

print(mean_absolute_error(val_y, val_predictions))



# =============================================================================
#  experimenting with different models
# =============================================================================

def get_mae(max_leaf_nodes, predictors_train, predictors_val, targ_train, targ_val):
    
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(predictors_train, targ_train)
    preds_val = model.predict(predictors_val)
    mae = mean_absolute_error(targ_val, preds_val)
    
    return(mae)


# compare MAE with differing values of max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))



# =============================================================================
# Random Forest
# =============================================================================



















































