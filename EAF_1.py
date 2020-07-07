#!/usr/bin/env python
# coding: utf-8

# In[182]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler


# In[213]:


df = pd.read_csv('sarda_data.csv', index_col=0)
df1 = pd.read_csv('dataToBeUsed_sarda_rev1.csv', index_col=0)
len(df1.columns)


# In[214]:


#data = pd.read_csv('https://www.dropbox.com/s/4jgheggd1dak5pw/data_visualization.csv?raw=1', index_col=0)
data = pd.read_csv('dataToBeUsed_sarda_rev2.csv', index_col=0)
scaler = MinMaxScaler() 
scaled_values = scaler.fit_transform(data) 
data.loc[:,:] = scaled_values
data.shape


# In[185]:


corr = data.corr()
fig = plt.figure(figsize=(60,20))
ax = fig.add_subplot(111)
cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,len(data.columns),1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(data.columns)
ax.set_yticklabels(data.columns)
plt.show()


# In[215]:


t = data[data.columns[1:]].corr()['SP. Power KWH'][:]
t.to_csv('featureCorrelation_rev1.csv') 


# In[152]:


#data[data.columns[1:]].corr()['Metal MT'][:]
#data[data.columns[1:]].corr()['Slag      MT'][:]
"""Top correlations for data frame"""
#data.corr().unstack().sort_values().drop_duplicates()
#data[data.columns[1:]].corr()['Coke::Coal'][:]
def str_div(num):
    split_num = num.split('/')
    return round(float(split_num[0])/float(split_num[1]),3)

def str_div(num):
    return round((float(num.split('/')[0]))/(float(num.split('/')[1]),3))


# In[ ]:


moistureGrade = pd.read_csv('EAF_moisture_grade.csv')


# In[157]:


moistureGrade_sum=moistureGrade.sum(axis = 1)


# In[159]:


moistureGrade_sum.to_csv('moistureGrade_sum.csv')


# In[112]:





# In[219]:


# Import pandas package  
import pandas as pd  
    
 #list(data) or 
list(data.columns) 


# In[149]:





# In[ ]:





# In[ ]:





# In[ ]:




