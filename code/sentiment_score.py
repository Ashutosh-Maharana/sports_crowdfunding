#%%
import pandas as pd
#%%
# Read in the main file
main_file = pd.read_csv("E:/PDS II/project-deliverable-2-bazinga/data/clean_data/final_dataset_textanalysis.csv")
#%%
# Read in the three files to merge
file1 = pd.read_csv("E:/PDS II/project-deliverable-2-bazinga/data/text_analysis_data/joy_sadness_raw_data_Grouped.csv")
file2 = pd.read_csv("E:/PDS II/project-deliverable-2-bazinga/data/text_analysis_data/pos_neg_raw_data_Grouped.csv")
file3 = pd.read_csv("E:/PDS II/project-deliverable-2-bazinga/data/text_analysis_data/trust_fear_raw_data_Grouped.csv")
#%%
# Merge the three files into one using the common identifier
merged_file = pd.merge(main_file, file1, on="CampaignURL", how="left")
merged_file = pd.merge(merged_file, file2, on="CampaignURL", how="left")
merged_file = pd.merge(merged_file, file3, on="CampaignURL", how="left")
#%%
# Select only the "sentiment" columns from the merged files
sentiment = merged_file[["CampaignURL", "joy count", "sadness count", "positive", "negative", "trust", "fear"]]
#%%
# Group by CampaignURL and sum the sentiment columns
sentiment_grouped = sentiment.groupby("CampaignURL").first()
#%%
# Join the grouped sentiment data with the main file using CampaignURL
main_file_with_sentiment = pd.merge(main_file, sentiment_grouped, on="CampaignURL", how="left")
#%%
# Drop duplicate CampaignURLs
main_file_with_sentiment = main_file_with_sentiment.drop_duplicates(subset="CampaignURL")
#%%
# Save the merged file with sentiments as a new CSV file
main_file_with_sentiment.to_csv("E:/PDS II/project-deliverable-2-bazinga/data/main_file_with_sentiment7.csv", index=False)

# %%
