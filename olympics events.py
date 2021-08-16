#!/usr/bin/env python
# coding: utf-8

# In[57]:


#Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[58]:


# load data set
athletes = pd.read_csv("E:/Python aniket/archive oly 20/athlete_events.csv")
regions = pd.read_csv("E:/Python aniket/archive oly 20/noc_regions.csv")


# In[59]:


athletes.head()


# In[60]:


regions.head()


# In[61]:


# join the data set
#pandas merge func

athletes_df = athletes.merge(regions, how = 'left', on ='NOC')
athletes.head()


# In[62]:


athletes_df.shape


# In[63]:


# coloum name
athletes_df.rename(columns={'region':'Region', 'notes':'Notes'}, inplace = True);


# In[64]:


athletes_df.head()


# In[65]:


athletes_df.info()


# In[66]:


athletes_df.describe()


# In[67]:


#chek null values

nan_values = athletes_df.isna()
nan_columns = nan_values.any()
nan_columns


# In[68]:


athletes_df.isnull().sum()


# In[69]:


# india details

athletes_df.query('Team == "India"').head(30)


# In[70]:


# Top countries participating
top_10_countries = athletes_df.Team.value_counts().sort_values(ascending = False).head(10)
top_10_countries


# In[71]:


# plot for 10 countries

plt.figure(figsize=(12,6))

plt.title('participation by country')
sns.barplot(x=top_10_countries.index, y=top_10_countries);


# In[72]:


# Age Distrubution of participation
# histogram
plt.figure(figsize=(12,6))
plt.title("Age distribution of the athletes")
plt.xlabel('Age')
plt.ylabel('number of particaipaints')
plt.hist(athletes_df.Age,bins = np.arange(10,80,2), color='violet', edgecolor = 'white'); 


# In[73]:


# winter oly
winter_sports = athletes_df[athletes_df.Season == 'winter'].Sport.unique()
winter_sports


# In[74]:


# Male & Female participaints

gender_counts = athletes_df.Sex.value_counts()
gender_counts


# In[75]:


#pie plot

plt.figure(figsize = (12,6))
plt.title('Gender Distrubution')
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=150, shadow=True);


# In[76]:


#total medels
athletes_df.Medal.value_counts()


# In[77]:


# Total no. of female athletes in each olympics.

female_participants = athletes_df[(athletes_df.Sex=='F')][['Sex','Year']]
female_participants = female_participants.groupby('Year').count().reset_index()

female_participants.tail()


# In[78]:


womenOlympics = athletes_df[(athletes_df.Sex == "F")]


# In[79]:


sns.set(style="darkgrid")
plt.figure(figsize=(20,10))
sns.countplot(x='Year', data=womenOlympics)
plt.title('women Participation')


# In[80]:


part = womenOlympics.groupby('Year')['Sex'].value_counts()
plt.figure(figsize=(20, 10))
part.loc[:,"F"].plot()
plt.title('plot of female Athletes over time')


# In[81]:


# Total no. of male athletes in each olympics.

male_participants = athletes_df[(athletes_df.Sex=='M')][['Sex','Year']]
male_participants = male_participants.groupby('Year').count().reset_index()

male_participants.tail()


# In[82]:


menOlympics = athletes_df[(athletes_df.Sex == "M")]


# In[83]:


sns.set(style="darkgrid")
plt.figure(figsize=(20,10))
sns.countplot(x='Year', data=menOlympics)
plt.title('men Participation')


# In[84]:


part = menOlympics.groupby('Year')['Sex'].value_counts()
plt.figure(figsize=(20, 10))
part.loc[:,"M"].plot()
plt.title('plot of male Athletes over time')


# In[85]:


# Gold medal athletes
goldMedals= athletes_df[(athletes_df.Medal=='Gold')]
goldMedals.head()


# In[86]:


goldMedals = goldMedals[np.isfinite(goldMedals['Age'])]


# In[87]:


#gold beyond 60
goldMedals['ID'][goldMedals['Age'] > 60].count()


# In[88]:


sporting_event = goldMedals['Sport'][goldMedals['Age'] > 60]
sporting_event


# In[89]:


#plot
plt.figure(figsize =(10,5))
plt.tight_layout()
sns.countplot(sporting_event)
plt.title('Gold medals Athletes over 60 years')


# In[90]:


# gold medals from Each Country
goldMedals.Region.value_counts().reset_index(name = "Medal").head(5)


# In[91]:


totalGoldMedals = goldMedals.Region.value_counts().reset_index(name = 'Medal').head()
g = sns.catplot(x='index', y='Medal', data=totalGoldMedals, height=5, kind='bar', palette='rocket')
g.despine(left=True)
g.set_xlabels('Top 5 countries')
g.set_ylabels('Gold Medals per Country')


# In[92]:


#Rio olym
max_year = athletes_df.Year.max()
print(max_year)

team_names = athletes_df[(athletes_df.Year == max_year) & (athletes_df.Medal == 'Gold')].Team

team_names.value_counts().head(10)


# In[93]:


sns.barplot(x=team_names.value_counts().head(20), y=team_names.value_counts().head(20).index)
plt.ylabel(None);
plt.xlabel('countrywise Medals for the year 2016');


# In[94]:


not_null_medals = athletes_df[(athletes_df['Height'].notnull()) & (athletes_df['Weight'].notnull())]


# In[95]:


plt.figure(figsize =(12, 10))
axis = sns.scatterplot(x="Height" , y="Weight", data=not_null_medals, hue='Sex')
plt.title('Height vs Weight of olympics Medalist')


# In[ ]:





# In[ ]:




