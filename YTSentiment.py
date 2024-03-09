#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn import linear_model

sent_obj = SentimentIntensityAnalyzer()
OLS = linear_model.LinearRegression()


def sent(input):
    sdict = sent_obj.polarity_scores(input)
    return sdict["compound"]


def analyze_data_set():
    # reads data set and does sentiment analysis on each element
    df = pd.read_csv("USvideos.csv",index_col=0)[["title","views","tags"]]
    l = [sent(i) for i in df.title] #takes a while
    
    # adds sentiment analysis column to the data frame
    df["title_sentiment"] = l
    # plt.plot(df["title_sentiment"],df["views"],"*")

    # maps to a linear regression model
    OLS.fit(df.title_sentiment.to_numpy().reshape(-1,1),df.views.to_numpy().reshape(-1,1))

def analyze_input(input):
    return OLS.predict(np.array(sent(input, sent_obj)).reshape(-1,1))


def main():
    input = "How to fix a car"
    analyze_data_set()
    analyze_input(input)


if __name__ == "__main__":
    main()




