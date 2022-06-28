#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing Data
import datetime
import numpy as np 
import pandas as pd
da=pd.read_csv("C:\\Users\\Sellomo\\Downloads\\maturity_assessments_dataset.csv",sep=';')
da.head()


# # Data Cleaning
# 

# In[5]:


#Applying time Stamp to the assessment_date
da["assessment_date_2"] = da["assessment_date"].apply(pd.to_datetime)
da


# In[8]:


#Cleaning/Correcting the Brasil/Brazil Syntax
da['country']=da['country'].replace (['Brasil'],'Brazil')


# In[10]:


#checking the change
da['country'].value_counts()


# # Questions

# #### Which client has conducted the most assessments in total? _Client 3_
# 

# In[25]:


da.groupby('client').count().sort_values(by=['tracc_practice'],ascending=False)


# #### Across how many countries are our clients assessing TRACC practices ? _24 Countries_
# 

# In[24]:


da.groupby('country').count()
da['country'].value_counts()
len(list(da['country'].unique()))


# #### How many assessments were conducted in total for all clients, after 31 March 2018 ? _2598 Assessments_
# 

# In[23]:


df2=da[da['assessment_date_2']>datetime.datetime(2018,3,31)]
df2.count()


# #### How many unique TRACC practices did Client 48 assess ? _347_
# 

# In[26]:


da.groupby("client").get_group('Client 48').groupby('tracc_practice').count()


# #### How many assessments were done for each practice in 2017 ? _3301_

# In[29]:


da3=da[da['assessment_date_2']>=datetime.datetime(2017,1,1)]
da4=da3[da3['assessment_date_2']<=datetime.datetime(2017,12,31)]
da4.groupby('tracc_practice').count()


# #### Which clients have achieved a maturity score greater than 2.5, for the 5S and Teamwork practices ? _25 clients_

# In[31]:


da5=da[da['tracc_maturity']>2.5]
da5


# In[54]:


da6_1=da5[(da5['tracc_practice']== '5S')]
da6_2=da5[(da5['tracc_practice']== 'Teamwork')]


# In[64]:


frames = [da6_2, da6_1]  
result = pd.concat(frames)


# In[68]:


result['client'].value_counts()


# In[ ]:




