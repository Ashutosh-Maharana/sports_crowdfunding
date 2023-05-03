#%%
import pandas as pd
import os
import matplotlib.pyplot as plt

#%%
wd = os.getcwd()
try:
    wd = wd.replace("/code", "")
except: 
    pass
os.chdir(wd)

df = pd.read_csv("{}/data/clean_data/final_dataset_textanalysis_sentiment_score.csv".format(os.getcwd()))
df = df[df['is_english'] == 1]

#%%
df['joy_sad'] = df.apply(lambda x: 'joy' if x['joy'] > x['sadness'] else 'sadness', axis=1)
df['pos_neg'] = df.apply(lambda x: 'positive' if x['positive'] > x['negative'] else 'negative', axis=1)
df['trust_fear'] = df.apply(lambda x: 'trust' if x['trust'] > x['fear'] else 'fear', axis=1)

# %%
##joy_sad_percentage values per SportName
# Create a pivot table to calculate the percentage of joy_sad values per SportName
pt = pd.pivot_table(df, index='SportName', columns='joy_sad', values='CampaignURL', aggfunc='count', fill_value=0)
pt['joy_sad_percentage'] = pt['joy'] / (pt['joy'] + pt['sadness']) * 100

# Filter the pivot table to exclude SportName values with 100% joy_sad_percentage
pt_filtered = pt[pt['joy_sad_percentage'] < 100]

# Create a cumulative bar chart of the joy_sad_percentage values per SportName
ax = pt_filtered['joy_sad_percentage'].sort_values(ascending=False).plot(kind='bar', stacked=True, width=0.8)

# Format the plot
ax.set_xlabel('Sport Name')
ax.set_ylabel('Percentage')
ax.set_title('Percentage of Joy and Sadness Scores per Sport Name (Excluding 100%)')
plt.tight_layout()
plt.show()
#%%
##pos_neg_percentage values per SportName
# Create a pivot table to calculate the percentage of pos_neg values per SportName
pt = pd.pivot_table(df, index='SportName', columns='pos_neg', values='CampaignURL', aggfunc='count', fill_value=0)
pt['pos_neg_percentage'] = pt['positive'] / (pt['positive'] + pt['negative']) * 100

# Filter the pivot table to only include sport names without 100% positive or negative scores
pt_filtered = pt[pt['pos_neg_percentage'] != 100]

# Create a cumulative bar chart of the pos_neg_percentage values per SportName
ax = pt_filtered['pos_neg_percentage'].sort_values(ascending=False).plot(kind='bar', stacked=True, width=0.8)

# Format the plot
ax.set_xlabel('Sport Name')
ax.set_ylabel('Percentage')
ax.set_title('Percentage of Positive and Negative Scores per Sport Name (Excluding 100%)')
plt.tight_layout()
plt.show()

#%%
##trust_fear_percentage values per SportName
# Create a pivot table to calculate the percentage of trust_fear values per SportName
pt = pd.pivot_table(df, index='SportName', columns='trust_fear', values='CampaignURL', aggfunc='count', fill_value=0)
pt['trust_fear_percentage'] = pt['trust'] / (pt['trust'] + pt['fear']) * 100

# Filter the pivot table to only include sport names without 100% trust or fear scores
pt_filtered = pt[pt['trust_fear_percentage'] != 100]

# Create a cumulative bar chart of the trust_fear_percentage values per SportName
ax = pt_filtered['trust_fear_percentage'].sort_values(ascending=False).plot(kind='bar', stacked=True, width=0.8)

# Format the plot
ax.set_xlabel('Sport Name')
ax.set_ylabel('Percentage')
ax.set_title('Percentage of Trust and Fear Scores per Sport Name (Excluding 100%)')
plt.tight_layout()
plt.show()

#%%
####joy_sad_percentage values per Country
# Create a pivot table to calculate the percentage of joy_sad values per SportName
pt = pd.pivot_table(df, index='Country', columns='joy_sad', values='CampaignURL', aggfunc='count', fill_value=0)
pt['joy_sad_percentage'] = pt['joy'] / (pt['joy'] + pt['sadness']) * 100

# Filter the pivot table to exclude SportName values with 100% joy_sad_percentage
pt_filtered = pt[pt['joy_sad_percentage'] < 100]

# Create a cumulative bar chart of the joy_sad_percentage values per SportName
ax = pt_filtered['joy_sad_percentage'].sort_values(ascending=False).plot(kind='bar', stacked=True, width=0.8)

# Format the plot
ax.set_xlabel('Sport Name')
ax.set_ylabel('Percentage')
ax.set_title('Percentage of Joy and Sadness Scores per Country (Excluding 100%)')
plt.tight_layout()

plt.show()

#%%
##pos_neg_percentage values per Country
# Create a pivot table to calculate the percentage of pos_neg values per SportName
pt = pd.pivot_table(df, index='Country', columns='pos_neg', values='CampaignURL', aggfunc='count', fill_value=0)
pt['pos_neg_percentage'] = pt['positive'] / (pt['positive'] + pt['negative']) * 100

# Filter the pivot table to only include sport names without 100% positive or negative scores
pt_filtered = pt[pt['pos_neg_percentage'] != 100]

# Create a cumulative bar chart of the pos_neg_percentage values per SportName
ax = pt_filtered['pos_neg_percentage'].sort_values(ascending=False).plot(kind='bar', stacked=True, width=0.8)

# Format the plot
ax.set_xlabel('Sport Name')
ax.set_ylabel('Percentage')
ax.set_title('Percentage of Positive and Negative Scores per Country (Excluding 100%)')
plt.tight_layout()
plt.show()

#%%
##trust_fear_percentage values per Country
# Create a pivot table to calculate the percentage of trust_fear values per SportName
pt = pd.pivot_table(df, index='Country', columns='trust_fear', values='CampaignURL', aggfunc='count', fill_value=0)
pt['trust_fear_percentage'] = pt['trust'] / (pt['trust'] + pt['fear']) * 100

# Filter the pivot table to only include sport names without 100% trust or fear scores
pt_filtered = pt[pt['trust_fear_percentage'] != 100]

# Create a cumulative bar chart of the trust_fear_percentage values per SportName
ax = pt_filtered['trust_fear_percentage'].sort_values(ascending=False).plot(kind='bar', stacked=True, width=0.8)

# Format the plot
ax.set_xlabel('Sport Name')
ax.set_ylabel('Percentage')
ax.set_title('Percentage of Trust and Fear Scores per Country (Excluding 100%)')
plt.tight_layout()
plt.show()


# %%
