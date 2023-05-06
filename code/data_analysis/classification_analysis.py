# #%%
import pandas as pd
import numpy as np
import os
import re
import time
import json
import nltk
# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
from gensim.test.utils import datapath
# spacy for lemmatization
import spacy
import matplotlib.pyplot as plt
# NLTK stopwords
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

#%%
# Load train and test data into 2 dataframs
# Map the text "Story_Original" data into both of these dataframes

# train split into X_train and Y_train
# test split into X_test and Y_test

# Transformations check
# Scaling - train, test combined or separate
#%%
# Normal NN
# MLPClassifier
# different hyperparameters
# Activation funciton list - [1, 2, 3]
# Hidden Layers list - []
# for loop - train, test, 
# AUC, accuracy, sensitivity, specificity -
# Train

#%%
# LSTM + GloVe vectors
