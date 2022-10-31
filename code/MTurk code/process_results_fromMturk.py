#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import numpy as np
import datetime
#%%
i = 0
j = 41

# with open ("results_after_"+str(i)+"_"+str(j)+".json", 'r') as fin:
#     data = json.load(fin)
    

with open ("results_after_tweets_dpr.json", 'r') as fin:
    data = json.load(fin) 

workers = []
workers_dict = {}
    
for hit in data:
    for a in hit['answers']:
        workers.append(a['workerID'])
    
#%%
unique_workers = list(np.unique(workers))

for i in unique_workers:
    workers_dict[i] =  []
    
#%%

for hit in data:
    for a in hit['answers']:
        
        start = datetime.datetime.strptime(a['AcceptTime'][:-6], '%Y-%m-%d %H:%M:%S')
        finish = datetime.datetime.strptime(a['SubmitTime'][:-6], '%Y-%m-%d %H:%M:%S')
        
        time = (finish - start).total_seconds() / 60.0
        workers_dict[a['workerID']].append(time)
        
#%%

#%%

# unique_workers = list(np.unique(workers))

# for i in unique_workers:
#     workers_dict[i] =  []
    
# def convert_label(d): 
#     if d['not_relevant']==True  and d['relevant']==False:
#         label = 'not_relevant'
#     elif d['not_relevant']==False  and d['relevant']==True:
#         label = 'relevant'
#     else:
#         print ("Something is wrong with labels")
#         print (d)
#     return label

# def convert_answers(a):
#     ans_list = []
#     results_dict = json.loads(a['answer'][1:-1])
#     workerid = a['workerID']
    
#     for i in range(3):
#         for j in range(5):
            
#             relevance_str = 'c'+str(i+1)+'relevance'+str(j+1)
#             ans_list.append(convert_label(results_dict[relevance_str]))
                
#     return workerid, ans_list


# for hit in data: 
#     for a in hit['answers']:
#         workerid, ans_list = convert_answers(a)
#         workers_dict[workerid].extend(ans_list)
        
# #%%

# for item in workers_dict.items(): 
    
#     if len(np.unique(item[1]))<2:
#         print(item)


