#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn import linear_model


# In[13]:


df = pd.read_csv("USvideos.csv",index_col=0)[["title","views","tags"]]


# In[17]:


sent_obj = SentimentIntensityAnalyzer()
def sent(input):
    sdict = sent_obj.polarity_scores(input)
    return sdict["compound"]


# In[25]:


l = [sent(i) for i in df.title] #takes a while


# In[23]:





# In[26]:


df["title_sentiment"] = l


# In[34]:


plt.plot(df["title_sentiment"],df["views"],"*")


# In[43]:


OLS = linear_model.LinearRegression()
OLS.fit(df.title_sentiment.to_numpy().reshape(-1,1),df.views.to_numpy().reshape(-1,1))


# In[63]:


OLS.predict(np.array(sent("hi there, ye who are destinced for death")).reshape(-1,1))


# In[ ]:




