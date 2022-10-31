#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from TwitterAPI import TwitterAPI, TwitterOAuth, TwitterRequestError, TwitterConnectionError, TwitterPager
import pandas as pd
import numpy as np
import json
import os
from download_one_conversation import download_conversation
from time import sleep
# consumer_key= "CONSUMER KEY"
# consumer_secret= "CONSUMER SECRET"
# access_token_key= "ACCESS TOKEN KEY"
# access_token_secret= "ACCESS TOKEN SECRET"
# api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret, api_version='2')

#%%

#  path to save convos
savepath = "../conversations/"
#%%
# load annotated data

path_todf = ""
df = pd.read_csv(path_todf)
    

# make a list of tweet ids

twids1 = list(df.tweet_id)


uniquetwids = list(np.unique(twids1))

# use tweet ids as conversation ids 

#  get conversations
#%%
non_convid_tweets = []
for conv_id in uniquetwids:
    
    filepath = savepath+str(conv_id)+'.jsonl'
    
    if os.path.exists(filepath):
        continue
    
    r = download_conversation(conv_id)
    
    if r==[]:
        non_convid_tweets.append(conv_id)
        continue
    #  store them
    
    with open(filepath, 'w') as outfile:
        for entry in r:
            json.dump(entry, outfile)
            outfile.write('\n')
    
    sleep(2)
   

# where tweeets ids were not conversation ids then if possible load tweet objects 


