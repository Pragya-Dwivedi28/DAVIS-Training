# -*- coding: utf-8 -*-
"""Python_Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-T_6_iUKLGetNqnclGX2ulNl7P-31z8Y
"""

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

from google.colab import drive
drive.mount('/content/drive')

auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

file_id = '1INJqiDXmL98BGXFBKsZ8VLGTGJjtTp9f'
downloaded = drive.CreateFile({'id': file_id})

file_id = '1fgsxmAOzrLrM1Kxq0o0ExE9XUzIB7A4B'
downloaded = drive.CreateFile({'id': file_id})

file_id = '1yqtS3RdwVWDyZP6CLp9MPYcrPhQCncij'
downloaded = drive.CreateFile({'id': file_id})

file_id = '1uS6T5cb1X312c3M-RySQUpLEsUHiKCgz'
downloaded = drive.CreateFile({'id': file_id})

file_id = '1I1sD12LvIYB28cETlewyMzwfkQSjYoI5'
downloaded = drive.CreateFile({'id': file_id})

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

# load the datasets

athletes = pd.read_csv('/content/drive/MyDrive/archive (2)/archive (4)/athlete_events.csv')
regions = pd.read_csv('/content/drive/MyDrive/archive (2)/archive (4)/noc_regions.csv')

athletes.head()

regions.head()

# Join the DataFrames
athletes_df = athletes.merge(regions, how='left', on ='NOC')
athletes_df.head()

athletes_df.shape

athletes_df.head()

athletes_df.info()

athletes_df.describe()

# Check null values
nan_values = athletes_df.isna()
nan_columns = nan_values.any()
nan_columns

athletes_df.isnull().sum()

# India details
athletes_df.query('Team == "India"').head(5)

# Japan details
athletes_df.query('Team == "Japan"').head(5)

# Top countries participating

top_10_countries = athletes_df.Team.value_counts().sort_values(ascending=False).head(10)
top_10_countries

# Plot for the top 10 countries
plt.figure(figsize=(12,6))
#plt.xticks(rotation=20)
plt.title("Overall Participation by Country")
sns.barplot(x= top_10_countries.index, y=top_10_countries, palette='Set2')

# Age distribution of the participants
plt.figure(figsize=(12,6))
plt.title("Age distribution of the athletes")
plt.xlabel('Age')
plt.ylabel('Number of participants')
plt.hist(athletes_df.Age, bins= np.arange(10,80,2), color='orange', edgecolor='white')

# Winter olympics sports
winter_sports = athletes_df[athletes_df.Season == 'Winter'].Sport.unique()
winter_sports

# Summer olympics sports
summer_sports = athletes_df[athletes_df.Season == 'Summer'].Sport.unique()
summer_sports

# Male and Female participants

gender_counts = athletes_df.Sex.value_counts()
gender_counts

#Pie plot for male and female athletes
plt.figure(figsize=(12,6))
plt.title("Gender distribution")
plt.pie(gender_counts, labels= gender_counts.index, autopct='%1.1f%%', startangle=150, shadow=True)

# Total medals
athletes_df.Medal.value_counts()

# Total number of female athletes in each olympics
female_participants = athletes_df[(athletes_df.Sex=='F') & (athletes_df.Season == 'Summer')][['Sex','Year']]
female_participants = female_participants.groupby('Year').count().reset_index()
female_participants.head()

#Another way to find the number of female athletes in each olympics
womenOlympics = athletes_df[(athletes_df.Sex == 'F') & (athletes_df.Season == 'Summer')]
womenOlympics

sns.set(style='darkgrid')
plt.figure(figsize=(20,10))
sns.countplot(x='Year', data = womenOlympics, palette = 'Spectral')
plt.title('Women Participation')

part = womenOlympics.groupby('Year')['Sex'].value_counts()
plt.figure(figsize=(20,10))
part.loc[:,'F'].plot()
plt.title('Plot of Female Athletes over time')

# Gold medal athletes
goldMedals = athletes_df[(athletes_df.Medal == 'Gold')]
goldMedals.head()

# take only values that are different from NaN
goldMedals = goldMedals[np.isfinite(goldMedals['Age'])]

# Gold beyond 60
goldMedals['ID'][goldMedals['Age']>60].count()

sporting_event = goldMedals['Sport'][goldMedals["Age"]>60]
sporting_event

# Plot for sporting event
plt.figure(figsize=(10,5))
plt.tight_layout()
sns.countplot(sporting_event)
plt.title('Gold Medals for Athletes over 60 years')

# Gold medals from each country

goldMedals.Region.value_counts().reset_index(name='Medal').head(5)

totalGoldMedals = goldMedals['Region'].value_counts().reset_index(name='Medal').head(6)
totalGoldMedals.columns = ['Country', 'Medal']  # Rename columns for clarity
g = sns.catplot(x="Country", y="Medal", data=totalGoldMedals,
                height=5, kind="bar", palette="rocket")

# Customize the plot
g.despine(left=True)
g.set_axis_labels("Top 5 Countries", "Number of Medals")
plt.title("Gold Medals per Country")

# Show the plot
plt.show()

# Rio olympics
max_year = athletes_df.Year.max()
print(max_year)
team_names = athletes_df[(athletes_df.Year == max_year)&(athletes_df.Medal=='Gold')].Team
team_names.value_counts().head(10)

# Assuming team_names is a Series or DataFrame column with team names
counts = team_names.value_counts().head(20)
sns.barplot(x=counts, y=counts.index, palette="viridis")
plt.xlabel('Countrywise Medals for the Year 2016')
plt.ylabel(None)
plt.title('Top 20 Teams by Medal Count')
plt.show()

not_null_medals = athletes_df[(athletes_df['Height'].notnull()) & (athletes_df['Weight'].notnull())]

plt.figure(figsize =(12,10))
axis = sns.scatterplot(x='Height', y='Weight', data=not_null_medals, hue='Sex')
plt.title("Height vs Weight of Olympic Medalists")