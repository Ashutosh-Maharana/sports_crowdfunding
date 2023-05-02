# %%
import pandas as pd
import spacy
# %%
# load spaCy's English model
nlp = spacy.load('en_core_web_sm')

# read the CSV file containing the text data
# %%
import os
cwd = os.getcwd()
cwd = cwd.replace("\\code", "")
cwd
# %%
df = pd.read_csv("{}\\data\\clean_data\\final_dataset_textanalysis_sentiment_score.csv".format(cwd))
# %%

# filter for English language stories
english_df = df[df['is_english'] == 1].copy()
# %%
# create columns to store named entity recognition results
for entity in ['Person', 'Organization', 'Geo', 'Group', 'Event', 'Product']:
    english_df[f'{entity}_Entity'] = ''

# loop through each story and perform named entity recognition using spaCy
for i, story in english_df['Story_Original'].iteritems():
    doc = nlp(story)
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            english_df.at[i, 'Person_Entity'] += f"{ent.text} ({ent.label_}), "
        elif ent.label_ == 'ORG':
            english_df.at[i, 'Organization_Entity'] += f"{ent.text} ({ent.label_}), "
        elif ent.label_ in ['GPE', 'LOC', 'FAC']:
            english_df.at[i, 'Geo_Entity'] += f"{ent.text} ({ent.label_}), "
        elif ent.label_ == 'NORP':
            english_df.at[i, 'Group_Entity'] += f"{ent.text} ({ent.label_}), "
        elif ent.label_ == 'EVENT':
            english_df.at[i, 'Event_Entity'] += f"{ent.text} ({ent.label_}), "
        elif ent.label_ == 'PRODUCT':
            english_df.at[i, 'Product_Entity'] += f"{ent.text} ({ent.label_}), "
# %%
english_df
# %%
# write the results to a new CSV file
english_df.to_csv("{}\\data\\text_analysis_data\\ner_results.csv".format(cwd))


# %%
