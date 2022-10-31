#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import requests
import os
import json
import pickle

# non_convid_tweets = <LOAD LIST OF TWEET IDS HERE>

#  get tweet object, get its conversation id, save conversation ids



bearer_token = ""


def create_url(non_convid_tweets, start_index, end_index):
    tweet_fields = "tweet.fields=conversation_id"
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    ids = "ids="
    for id in non_convid_tweets[start_index:end_index]:
        ids = ids+str(id)+',' 
    ids = ids[:-1]
    # You can adjust ids to include a single Tweets.
    # Or you can add to up to 100 comma-separated IDs
    url = "https://api.twitter.com/2/tweets?{}&{}".format(ids, tweet_fields)
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()
#%%
conv_ids = []

# url = create_url(non_convid_tweets, 0, len(non_convid_tweets))
# headers = create_headers(bearer_token)
# json_response = connect_to_endpoint(url, headers)
   
# for tw in json_response['data']:
#     conv_ids.append(tw['conversation_id'])

# conv_ids = []
n = 100
for i in range(n,len(non_convid_tweets),n):
    
    print(i)
    
    filepath = "non_conv_id_tweet_obj/non_conv_id_tweet_obj2_"+str(i-n)+"_"+str(i)+".json"
    url = create_url(non_convid_tweets, i-n, i)
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
   
    with open(filepath, 'w') as outfile:
        json.dump(json_response, outfile)
            
   
    for tw in json_response['data']:
        conv_ids.append(tw['conversation_id'])



conv_id_tw_path = "conv_ids_new.pkl"
with open(conv_id_tw_path, 'wb') as fp:
    pickle.dump(conv_ids, fp)


