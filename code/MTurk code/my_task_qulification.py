#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import boto3


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
# questions = open(file='question2.xml', mode='r').read()
# answers = open(file='answer2.xml', mode='r').read()

# qual_response = mturk.create_qualification_type(
#                         Name='Determine claim-tweet relevance qualification test',
#                         Keywords='relevance, tweets, misinformation, qualification',
#                         Description='This is a qualification HIT',
#                         QualificationTypeStatus='Active',
#                         Test=questions, #The Test argument needs to be a QuestionForm datatype
#                         AnswerKey=answers, #AnswerKey data structure
#                         TestDurationInSeconds=60*10) # 10 minutes


# print(qual_response['QualificationType']['QualificationTypeId'])

# qid = qual_response['QualificationType']['QualificationTypeId']


#%%
# hit = mturk.create_hit(
#         Reward='0.01',
#         LifetimeInSeconds=3600,
#         AssignmentDurationInSeconds=600,
#         MaxAssignments=9,
#         Question=questions,
#         Title='A HIT with a qualification test7',
#         Description='A test HIT that requires a certain score from a qualification test to accept.',
#         Keywords='boto, qualification, test',
#         AutoApprovalDelayInSeconds=0,
#         QualificationRequirements=[{'QualificationTypeId':qid,
#                                     'Comparator': 'EqualTo',
#                                     'IntegerValues':[100]}]
#         )

# "Comparator": "GreaterThan",
# "IntegerValues": [0],
# "ActionsGuarded": "DiscoverPreviewAndAccept"


#associate_qualification_with_worker

#%%

html_layout = open('MyClaimTweetTask.html', 'r').read()
QUESTION_XML = """<HTMLQuestion xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2011-11-11/HTMLQuestion.xsd">
        <HTMLContent><![CDATA[{}]]></HTMLContent>
        <FrameHeight>650</FrameHeight>
        </HTMLQuestion>"""
question_xml = QUESTION_XML.format(html_layout)

TaskAttributes = {
    #  how many workers can take each HIT
    'MaxAssignments': 3, # 10 for sandbox, and less for actual task           
    # How long the task will be available on MTurk - 4 days   
    'LifetimeInSeconds': 60*60*24*4,
    # How long Workers have to complete each item (30 minutes)
    'AssignmentDurationInSeconds': 60*30,
    # This is the amount of time you have to reject a Worker's assignment after they submit the assignment.  - 3 days
    'AutoApprovalDelayInSeconds': 60*60*24*3,
    # The reward you will offer Workers for each response
    'Reward': '2.05',                     
    'Title': 'Claim-tweet relevance task',
    'Keywords': 'relevance, tweet, claim',
    'Description': 'Tag whether a tweet is relevant to a given claim',
    'QualificationRequirements':[{'QualificationTypeId':qid,
                                    'Comparator': 'GreaterThan',
                                    'IntegerValues':[70]}, # 5 out of 7 qs right
                                 {'QualificationTypeId':'00000000000000000040',
                                    'Comparator': 'GreaterThan',
                                    'IntegerValues':[100]},
                                 {'QualificationTypeId':'000000000000000000L0',
                                    'Comparator': 'GreaterThan',
                                    'IntegerValues':[95]},
                                 {'QualificationTypeId':'00000000000000000071',
                                    'Comparator': 'In',
                                    'LocaleValues':[{'Country':"US"}, {'Country':"GB"}, {'Country':"AG"}, {'Country':"AT"},
                                                    {'Country':"BS"}, {'Country':"BB"}, {'Country':"BZ"}, {'Country':"CA"},
                                                    {'Country':"DM"}, {'Country':"GD"}, {'Country':"GY"}, {'Country':"IE"},
                                                    {'Country':"JM"}, {'Country':"MT"}, {'Country':"NZ"}, {'Country':"TT"},
                                                    {'Country':"LC"}, {'Country':"VC"}, {'Country':"KN"}
                                                    ]
                                 }]
                                 
                                
}
# Worker_​NumberHITsApproved  00000000000000000040
# Worker_​PercentAssignmentsApproved  000000000000000000L0
# https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html#ApiReference_QualificationType-IDs
#%%

import pandas as pd

path = "file.csv"

data = pd.read_csv(path)
data_list = data.values.tolist()

#%%
results = []
hit_type_id = ''
# i = 0
# j = 41
for input_instance in data_list:
    
    new_question_xml = question_xml.replace('${claim1}',input_instance[0])
    
    new_question_xml = new_question_xml.replace('${c1tweet0}',input_instance[1])
    new_question_xml = new_question_xml.replace('${c1tweet1}',input_instance[2])
    new_question_xml = new_question_xml.replace('${c1tweet2}',input_instance[3])
    new_question_xml = new_question_xml.replace('${c1tweet3}',input_instance[4])
    new_question_xml = new_question_xml.replace('${c1tweet4}',input_instance[5])
    
    new_question_xml = new_question_xml.replace('${claim2}',input_instance[6])
    
    new_question_xml = new_question_xml.replace('${c2tweet0}',input_instance[7])
    new_question_xml = new_question_xml.replace('${c2tweet1}',input_instance[8])
    new_question_xml = new_question_xml.replace('${c2tweet2}',input_instance[9])
    new_question_xml = new_question_xml.replace('${c2tweet3}',input_instance[10])
    new_question_xml = new_question_xml.replace('${c2tweet4}',input_instance[11])
   
    new_question_xml = new_question_xml.replace('${claim3}',input_instance[12])
    
    new_question_xml = new_question_xml.replace('${c3tweet0}',input_instance[13])
    new_question_xml = new_question_xml.replace('${c3tweet1}',input_instance[14])
    new_question_xml = new_question_xml.replace('${c3tweet2}',input_instance[15])
    new_question_xml = new_question_xml.replace('${c3tweet3}',input_instance[16])
    new_question_xml = new_question_xml.replace('${c3tweet4}',input_instance[17])
    
    response = mturk.create_hit(
        **TaskAttributes,
        Question=new_question_xml
    )
    hit_type_id = response['HIT']['HITTypeId']
    
    results.append({
        
        'input': input_instance,
        'hit_id': response['HIT']['HITId']
    })
    
# print("You can view the HITs here:")
# print("https://workersandbox.mturk.com/mturk/preview"+"?groupId={}".format(hit_type_id))

print (hit_type_id)

import json
#with open ("results_before_"+str(i)+"_"+str(j)+".json", 'w') as fout:
#     json.dump(results, fout)

with open ("results.json", 'w') as fout:
    json.dump(results, fout)