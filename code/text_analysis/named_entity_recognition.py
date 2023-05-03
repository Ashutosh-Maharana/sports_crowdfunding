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
entities = ['PERSON', 'ORG', 'PRODUCT', 'EVENT', 'MONEY', 'DATE', 'TIME', 'GPE', 'LOC', 'NORP']
for entity in entities:
    english_df[f'{entity}_Entity'] = ''

# loop through each story and perform named entity recognition using spaCy
for i, story in english_df['Story_Original'].iteritems():
    doc = nlp(story)
    for ent in doc.ents:
        if ent.label_ in ['PERSON']:
            english_df.at[i, 'PERSON_Entity'] += f"{ent.text} ({ent.label_}), "
        elif ent.label_ in ['ORG']:
            english_df.at[i, 'ORG_Entity'] += f"{ent.text} ({ent.label_}), "
        elif ent.label_ in ['PRODUCT']:
            english_df.at[i, 'PRODUCT_Entity'] += f"{ent.text} ({ent.label_}), "
        elif ent.label_ in ['EVENT']:
            english_df.at[i, 'EVENT_Entity'] += f"{ent.text} ({ent.label_}), "
        elif ent.label_ in ['MONEY']:
            english_df.at[i, 'MONEY_Entity'] += f"{ent.text} ({ent.label_}), "
        elif ent.label_ in ['DATE']:
            english_df.at[i, 'DATE_Entity'] += f"{ent.text} ({ent.label_}), "
        elif ent.label_ in ['TIME']:
            english_df.at[i, 'TIME_Entity'] += f"{ent.text} ({ent.label_}), "
        elif ent.label_ in ['GPE', 'LOC','FAC']:
            english_df.at[i, 'LOC_Entity'] += f"{ent.text} ({ent.label_}), "
        elif ent.label_ in ['NORP']:
            english_df.at[i, 'NORP_Entity'] += f"{ent.text} ({ent.label_}), "
# %%
english_df.columns
# %%

df2 = english_df.filter(['CampaignURL','SportName','City','State','Country','TeamOrAthlete','language','PERSON_Entity', 'ORG_Entity','PRODUCT_Entity', 'EVENT_Entity', 'MONEY_Entity', 'DATE_Entity','TIME_Entity', 'GPE_Entity', 'LOC_Entity', 'NORP_Entity'], axis=1)
print(df2)
# %%
# write the results to a new CSV file
df2.to_csv("{}\\data\\text_analysis_data\\ner_results.csv".format(cwd))


# %%
