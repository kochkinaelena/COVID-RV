#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import boto3
import xmltodict
import json

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

#%%
# i = 0
# j = 35
# results = []
# with open ("results_before_"+str(i)+"_"+str(j)+".json", 'r') as fin:
#     for element in fin:
#         print("hi")
#         results=json.loads(element)
        
        
        
with open ("results_before_newer_tweets_dpr.json", 'r') as fin:
    for element in fin:
        print("hi")
        results=json.loads(element)
        
#%%

for item in results:    
    # Get the status of the HIT
    hit = mturk.get_hit(HITId=item['hit_id'])
    item['status'] = hit['HIT']['HITStatus']
    # Get a list of the Assignments that have been submitted
    assignmentsList = mturk.list_assignments_for_hit(
        HITId=item['hit_id'],
        AssignmentStatuses=['Submitted', 'Approved'],
        MaxResults=10
    )
    assignments = assignmentsList['Assignments']
    item['assignments_submitted_count'] = len(assignments)
    answers = []
    for assignment in assignments:
    
        # Retreive the attributes for each Assignment
        worker_id = assignment['WorkerId']
        assignment_id = assignment['AssignmentId']
        
        # Retrieve the value submitted by the Worker from the XML
        answer_dict = xmltodict.parse(assignment['Answer'])
        answer = answer_dict['QuestionFormAnswers']['Answer']['FreeText']
        
        my_answer_dict = {'workerID':worker_id, 'answer':answer, 'AcceptTime':assignment['AcceptTime'], 'SubmitTime':assignment['SubmitTime']}
        
        answers.append(my_answer_dict)
        
        # Approve the Assignment (if it hasn't been already)
        if assignment['AssignmentStatus'] == 'Submitted':
            mturk.approve_assignment(
                AssignmentId=assignment_id,
                OverrideRejection=False
            )
    
    # Add the answers that have been retrieved for this item
    item['answers'] = answers
    print(len(answers))
    # if len(answers) > 0:
    #     item['avg_answer'] = sum(answers)/len(answers)
# print(json.dumps(results,indent=2))
#%% 
# with open ("results_after_"+str(i)+"_"+str(j)+".json", 'w') as fout:
#     json.dump(results, fout, default=str)
    
with open ("results_after_tweets_dpr.json", 'w') as fout:
    json.dump(results, fout, default=str)