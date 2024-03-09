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

def sent_string(sentiment):  #takes in the output from the sent function
    if sentiment > 0.05:
        return "overall positive"   #feel free to change the strings if you want.
    elif sentiment < -.05:
        return "overall negative"
    else:
        return "neutral"


def analyze_data_set():
    # reads data set and does sentiment analysis on each element
    df = pd.read_csv("data/USvideos.csv",index_col=0)[["title","views","tags"]]
    l = [sent(i) for i in df.title] #takes a while
    
    # adds sentiment analysis column to the data frame
    df["title_sentiment"] = l
    # plt.plot(df["title_sentiment"],df["views"],"*")

    # maps to a linear regression model
    OLS.fit(df.title_sentiment.to_numpy().reshape(-1,1),df.views.to_numpy().reshape(-1,1))


def analyze_input(input):
    # Returns a string. 
    array_result = OLS.predict(np.array(sent(input)).reshape(-1,1))
    array_string = np.array2string(array_result, precision=0, separator=',').replace('[', '').replace(']', '').replace('.', '')
    return array_string


def main():
    input = ""
    analyze_data_set()
    print(f"For input: '{input}' the result of analysis is: {analyze_input(input)}")


if __name__ == "__main__":
    main()




