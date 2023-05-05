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