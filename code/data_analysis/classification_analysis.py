#%%
import pandas as pd
import numpy as np
import os
import re
import time
import json
import matplotlib.pyplot as plt
#Neural Network
import sklearn
from sklearn import metrics
from sklearn.neural_network import MLPRegressor
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

#%%
wd = os.getcwd()
try:
    wd = wd.replace("/code", "")
except: 
    pass
os.chdir(wd)
#%%
# Load train and test data into 2 dataframs
# Map the text "Story_Original" data into both of these dataframes

train_df = pd.read_csv("{}/data/data_analysis/final_data_train.csv".format(os.getcwd()))
test_df = pd.read_csv("{}/data/data_analysis/final_data_test.csv".format(os.getcwd()))
original_df = pd.read_csv("{}/data/clean_data/final_dataset_textanalysis_sentiment_score_updated.csv".format(os.getcwd()))

pd.read_csv("{}/data/clean_data/final_dataset_textanalysis_sentiment_score.csv".format(os.getcwd()))

# train split into X_train and Y_train
# test split into X_test and Y_test

train_df= pd.merge(train_df, original_df[["CampaignURL", "Story_Original"]], on="CampaignURL", how="left")
test_df = pd.merge(test_df, original_df[["CampaignURL", "Story_Original"]], on="CampaignURL", how="left")

#%%
# Split data into training and testing

X_train, Y_train = (train_df[['Wordcount', 'NarcissismFactor', 'joy',
       'sadness', 'negative', 'positive', 'fear', 'trust','numSupporters','FundingGoalAdjusted','TeamOrAthlete']], train_df.Success )

X_test, Y_test = (test_df[['Wordcount', 'NarcissismFactor', 'joy',
       'sadness', 'negative', 'positive', 'fear', 'trust','numSupporters','FundingGoalAdjusted','TeamOrAthlete']], test_df.Success )

#%%
# one-hot encode the TeamOrAthlete column in the train and test datasets
X_train = pd.concat([X_train, pd.get_dummies(train_df['TeamOrAthlete'], prefix='TeamOrAthlete')], axis=1)
X_test = pd.concat([X_test, pd.get_dummies(test_df['TeamOrAthlete'], prefix='TeamOrAthlete')], axis=1)

# Drop the original TeamOrAthlete column from the train and test datasets
X_train.drop('TeamOrAthlete', axis=1, inplace=True)
X_test.drop('TeamOrAthlete', axis=1, inplace=True)

#%%
# Transformations check
# Scaling - train, test combined or separate
scaler = preprocessing.StandardScaler()
scaler.fit(X_train)

# Perform the standardization process
X_train_std = scaler.transform(X_train)
X_test_std = scaler.transform(X_test)

#%%
# AUC, accuracy, sensitivity, specificity -
# Define lists for activation functions and hidden layers
activation_funcs = ['relu', 'logistic', 'tanh']
hidden_layers = [(50,50), (100,100), (50,100)]

# Train and test the neural network for different combinations of activation functions and hidden layers
for af in activation_funcs:
    for hl in hidden_layers:
        # Train and predict using the neural network
        nnclass = MLPClassifier(activation=af, solver='sgd', hidden_layer_sizes=hl)
        nnclass.fit(X_train_std, Y_train)
        nnclass_pred = nnclass.predict(X_test_std)
        
        # Evaluate the performance of the neural network
        cm = metrics.confusion_matrix(Y_test, nnclass_pred)
        print(f"Activation Function: {af}, Hidden Layers: {hl}")
        print("Confusion Matrix:")
        print(cm)
        plt.matshow(cm)
        plt.title(f"Confusion Matrix: Activation Function: {af}, Hidden Layers: {hl}")        
        plt.xlabel('Actual Value')
        plt.ylabel('Predicted Value')
        plt.show()
        print(metrics.classification_report(Y_test, nnclass_pred))
#%%
# LSTM + GloVe vectors
