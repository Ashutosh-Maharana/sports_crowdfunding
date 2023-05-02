#%%
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
# Plotting tools
import pyLDAvis
import pyLDAvis.gensim  # don't skip this
import matplotlib.pyplot as plt

# NLTK stopwords
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
%matplotlib inline

wd = os.getcwd()
try:  
    wd = wd.replace("/code", "")
except:
    pass

os.chdir(wd)

#%%
def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))  # deacc=True removes punctuations

# Initialize spacy 'en' model, keeping only tagger component (for efficiency)
# python3 -m spacy download en
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]

def make_bigrams(texts):
    return [bigram_mod[doc] for doc in texts]

def make_trigrams(texts):
    return [trigram_mod[bigram_mod[doc]] for doc in texts]

def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV', 'NUM', 'PRON']):
    """https://spacy.io/api/annotation"""
    texts_out = []
    for sent in texts:
        doc = nlp(" ".join(sent)) 
        texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
    return texts_out

#%%
# Loading Data Frame from clean data folder

df = pd.read_csv("{}/data/clean_data/final_dataset_textanalysis_sentiment_score.csv".format(os.getcwd()))
df.head()
# %%
data = df['Story_Original'].values.tolist()
# Remove new line characters
data = [re.sub('\s+', ' ', str(sent)) for sent in data]
# Remove distracting single quotes
data = [re.sub("\'", "", str(sent)) for sent in data]
data_words = list(sent_to_words(data))
# Build the bigram and trigram models
bigram = gensim.models.Phrases(data_words) # higher min_count or higher threshold fewer phrases.
# Faster way to get a sentence clubbed as a trigram/bigram
bigram_mod = gensim.models.phrases.Phraser(bigram)
# Remove Stop Words
data_words_nostops = remove_stopwords(data_words)
# Form Bigrams
data_words_bigrams = make_bigrams(data_words_nostops)
# Do lemmatization keeping only noun, adj, vb, adv
data_lemmatized = lemmatization(data_words_bigrams, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV', 'NUM', 'PRON'])
id2word = corpora.Dictionary(data_lemmatized)
# Create Corpus
texts = data_lemmatized
# # Term Document Frequency
corpus = [id2word.doc2bow(text) for text in texts]

#%%
# Build LDA model
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                        id2word=id2word,
                                        num_topics=10, 
                                    #    random_state=100,
                                    #    update_every=1,
                                    #    chunksize=100,
                                        passes=5,
                                        alpha='auto',
                                        per_word_topics=True)

#%%
print(lda_model.print_topics())

#%%
pyLDAvis.enable_notebook()
vis = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
vis
#%%
vis.save_html("{}/data/topic_modeling/lda_10.json".format(wd))
# %%
vis
# %%
