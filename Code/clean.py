# Importing libraries
import pandas as pd
import numpy as np

# Read csv file into a pandas dataframe
df = pd.read_csv("E:/4th year-1st semester/Thesis/Prediction of depression level from user's facebook post/Test/general_tweets.csv")

# Take a look at the first few rows
print(df.head())

# Looking at the columns
print(df['message'])
print(df['message'].isnull())

# Looking at the lbl column
print(df['label'])
print(df['label'].isnull())

# Making a list of missing value types
missing_values = ["n/a", "na", "--"]
df = pd.read_csv("E:/4th year-1st semester/Thesis/Prediction of depression level from user's facebook post/Test/general_tweets.csv", na_values = missing_values)

# Looking at the  column
print(df['message'])
print(df['message'].isnull())

# Detecting numbers
cnt=0
for row in df['label']:
    try:
        int(row)
        df.loc[cnt, 'label']=np.nan
    except ValueError:
        pass
    cnt+=1

# Total missing values for each feature
print(df.isnull().sum())

# Any missing values?
print(df.isnull().values.any())

# Total number of missing values
print(df.isnull().sum().sum())

# Replace missing values with a number
df['message'].fillna('NA', inplace=True)