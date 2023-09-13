#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv(r"C:\Users\selva\OneDrive\Desktop\My Uber Drives - 2016.csv")


# In[2]:


data.tail(10)


# In[3]:


data.head(10)


# In[4]:


data.info()


# In[5]:


data.isnull().sum()


# In[6]:


sns.heatmap(data.isnull(),yticklabels=False,cmap="viridis")


# In[7]:


df=data.dropna()
data.describe()


# In[8]:


df.describe()


# In[9]:


sns.countplot(x='CATEGORY*',data=data)


# In[10]:


data=data.dropna()
sns.heatmap(data.isnull(),yticklabels=False,cmap="viridis")


# In[11]:


data[data['START*']=='San Francisco']


# In[12]:


data['MILES*'].plot.hist()


# In[13]:


data['PURPOSE*'].value_counts().plot(kind='bar',figsize=(10,5),color='blue')


# In[14]:


data['START*'].value_counts().plot(kind='bar',figsize=(25,5),color='red')


# In[15]:


df=pd.DataFrame(data['MILES*'].groupby(data['PURPOSE*']).sum())
df.plot(kind='bar')
plt.show()


# In[16]:


df=df.reset_index()
sns.barplot(x=df['MILES*'],y=df['PURPOSE*'])


# In[17]:


df=data.groupby(['CATEGORY*']).sum()
Business=df.iloc[0,0]/(df.iloc[0,0]+df.iloc[1,0])
Personal=df.iloc[1,0]/(df.iloc[0,0]+df.iloc[1,0])
print("Business:",Business)
print("Personal:",Personal)


# In[18]:


group_by_file=data.groupby(by=['CATEGORY*'])
set_data_count=group_by_file.count()
set_data_avg=group_by_file.mean()
print(set_data_count)
print(set_data_avg)


# In[21]:


data['STOP*'].value_counts().plot(kind='bar',figsize=(25,5),color='green')


# In[22]:


group_by_file=data.groupby(by=['START*'])
set_data_count=group_by_file.count()
set_data_avg=group_by_file.mean()
print(set_data_count)
print(set_data_avg)


# In[ ]:




