#%% 
import os
import time
import gc

import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV, cross_val_score

#%%
PATH = r'/home/hq/git/udemy-recs/movielens-20m-dataset'

# %%
print(os.listdir(PATH))

# %%
df = pd.read_csv(os.path.join(PATH, 'rating.csv'))
df.head(3)


###### PREPROCESSING ######

# %%
df.drop('timestamp',axis=1,inplace=True)
# %%
df.isna().any()
# %%
df['userId']=df['userId'].apply(lambda x:x-1) #чтобы 0 начинался с 0 в numpy
df.head(5)
# %%


# %%

# %%
