#!/usr/bin/env python
# coding: utf-8

# In[1]:


path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'


# In[2]:


open(path).readline()


# In[3]:


from pandas import DataFrame, Series


# In[2]:


import pandas as pd


#  import pandas as pd

#  ##  I could not get the path from the book to work so I downloaded csv's from the website linked where applicable and uploaded them to my juypiter notebook.
#     

# In[5]:


frame = DataFrame(records)


# In[10]:


movies = pd.read_csv('movies.csv')


# In[12]:


ratings = pd.read_csv('ratings.csv')


# In[16]:


ratings[:5]


# In[17]:


movies[:5]


# In[25]:


names2018 = pd.read_csv('yob2018.csv')


# In[31]:


names2018.rename(columns={"ID": "births","Name":"name","Sex":"sex"}, inplace = True) 


# In[32]:


names2018


# In[33]:


names2018.groupby('sex').births.sum()


# In[4]:


# 2010 is the last available year right now
years = range(1880, 2011)
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
 path = 'names/yob%d.txt' % year
 frame = pd.read_csv(path, names=columns)
 frame['year'] = year
 pieces.append(frame)


# In[5]:


names = pd.concat(pieces, ignore_index=True)


# In[6]:


names


# In[19]:


total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)


# In[20]:


total_births.tail()


# In[9]:


def add_prop(group):
 # Integer division floors
 births = group.births.astype(float)
 group['prop'] = births / births.sum()
 return group
names = names.groupby(['year', 'sex']).apply(add_prop)


# In[11]:


import numpy as np


# In[12]:


np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1)


# In[31]:


def get_top1000(group):
 return group.sort_index(axis=1,level=2, ascending=False)[:1000]
grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)


# In[32]:


top1000


# In[33]:


boys = top1000[top1000.sex == 'M']


# In[34]:


girls = top1000[top1000.sex == 'F']


# In[35]:


total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)


# In[ ]:




