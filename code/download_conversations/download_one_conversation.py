#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# conversation_id = "1270293162486050817"

import requests
import os
import json
from copy import deepcopy
from time import sleep

bearer_token = ""




# query_params = {"next_token": "b26v89c19zqg8o3fo71h69o6bpgw9bb7tdg81p7f6067x",'query': 'conversation_id:1227998026658086921','start_time':'2020-01-01T17:19:07.000Z','max_results':'500','tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,source,text,withheld'}


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers, params):
    search_url = "https://api.twitter.com/2/tweets/search/all"
    response = requests.request("GET", search_url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def download_conversation(conversation_id):
    responses = []
    search_url = "https://api.twitter.com/2/tweets/search/all"
    query_str = 'conversation_id:'+str(conversation_id)
    query_params = {'query': query_str,'start_time':'2020-01-01T17:19:07.000Z','max_results':'100','tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,source,text,withheld'}

    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(search_url, headers, query_params)
    sleep(2)
    
    if json_response['meta']['result_count']==0:
        sleep(2)
        return []
    
    responses.extend(json_response['data'])
    
    while "next_token" in list(json_response['meta'].keys()):
        sleep(2)
        print ("more")
        query_params = {"next_token": json_response['meta']["next_token"],'query': query_str,'start_time':'2020-01-01T17:19:07.000Z','max_results':'100','tweet.fields': 'attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,source,text,withheld'}
        headers = create_headers(bearer_token)
        json_response = connect_to_endpoint(search_url, headers, query_params)
        responses.extend(deepcopy(json_response['data']))
        
    
    return responses

    # print(json.dumps(, indent=4, sort_keys=True))
    
# def save_conversation_to_json(json_response, path)
# conversation_id = 1221484214228529153
# r = download_conversation(conversation_id)





