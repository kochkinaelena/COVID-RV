#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import numpy as np
import pandas as pd
#%%
def convert_label(d): 
    if d['not_relevant']==True  and d['relevant']==False:
        label = 'not_relevant'
    elif d['not_relevant']==False  and d['relevant']==True:
        label = 'relevant'
    else:
        print ("Something is wrong with labels")
        print (d)
    return label
#%%
# claim, tweet, label, agreement, number of times link_opened, number of issues, 

#  +all entered comments collect in one list

# i = 0
# j = 41

# with open ("results_after_"+str(i)+"_"+str(j)+".json", 'r') as fin:
#     data1 = json.load(fin)
i = 0
j = 5

# with open ("results_after_"+str(i)+"_"+str(j)+".json", 'r') as fin:
#     data1 = json.load(fin)  
    
    
with open ("results_after_tweets.json", 'r') as fin:
    data1 = json.load(fin) 
# merge the two
# data1.extend(data2)
#%%
# all_claims = []
# all_tweets = []
# all_labels = []
# all_nlinks = []
# all_issues = [] 
all_rows = []
all_comments = []

for row in data1:
    inputs = row['input']
    answers =  row['answers']
    
    for ans in answers:
        results_dict = json.loads(ans['answer'][1:-1])
        if 'explanation' in list(results_dict.keys()):
            all_comments.append(results_dict['explanation']) 
    
    for i in range(3):
        for j in range(5):
        
            claim = inputs[i*6]
            tweet = inputs[i*6+j+1]
            
            ans_list = []
            link_list = []
            issue_list = []
            for ans in answers:
                results_dict = json.loads(ans['answer'][1:-1])
                relevance_str = 'c'+str(i+1)+'relevance'+str(j+1)
                ans_list.append(convert_label(results_dict[relevance_str]))
                
                check_str = "checkboxes"+'c'+str(i+1)+'t'+str(j)
                check2_str = "checkboxes2"+'c'+str(i+1)+'t'+str(j)
                
                link_list.append(results_dict[check2_str]['1'])
                issue_list.append(results_dict[check_str]['1'])
            
            label = max(set(ans_list), key = ans_list.count)
            
            agreement = ans_list.count(label)/len(ans_list)
    
            link_opened = np.sum(link_list)
            
            issues = np.sum(issue_list)
            
            new_row = [claim, tweet, label, agreement, link_opened, issues]
            all_rows.append(new_row)


df = pd.DataFrame(all_rows, columns = ['claim', 'tweet', 'label', 'agreement', 'number_of_times_link_opened', 'number_of_issues'])

df.to_csv("dataset.csv")
# save


#  what is the percentage of non relevant labels 
# then create the dataset of diff between dated and not dated to release 

# then consider another way of generating pairs 
#  how to come up with more claims to label

