#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import boto3
import xmltodict
import json
import datetime

region_name = 'us-east-1'
aws_access_key_id = ''
aws_secret_access_key = ''

# endpoint_url = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'

# Uncomment this line to use in production
endpoint_url = 'https://mturk-requester.us-east-1.amazonaws.com'

mturk = boto3.client(
    'mturk',
    endpoint_url=endpoint_url,
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)


# i = 0
# j = 5

# with open ("results_before_"+str(i)+"_"+str(j)+".json", 'r') as fin:
#     for element in fin:
#         print("hi")
#         results=json.loads(element)
        


with open ("results_before_newer_tweets.json", 'r') as fin:
    for element in fin:
        print("hi")
        results=json.loads(element)

for item in results: 
    
    hit_id = item['hit_id']
    response = mturk.update_expiration_for_hit(HITId=hit_id, ExpireAt=datetime.datetime(2021, 1, 1))
    