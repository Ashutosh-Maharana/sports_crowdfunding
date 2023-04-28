#%%
# Loading libraries
import pandas as pd
import numpy as np
import os

# Project Directory
cwd = os.getcwd()
cwd = cwd.replace("/code", "")
#%%

# Loading the final dataset
df = pd.read_csv("{}/data/clean_data/final_dataset_analysis.csv".format(cwd))

# %%
df.describe()
# %%
