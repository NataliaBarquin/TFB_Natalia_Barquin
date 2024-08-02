from pydantic import BaseModel, Field
from pydantic_xml import BaseXmlModel, attr, element
from typing import List, Optional
import pandas as pd

from aux.xml.read.train import NlmQuestions
from xsdata.formats.dataclass.parsers import XmlParser

import json


# The XML string you want to parse
file_path = 'data/xml/train_dataset/cleaned/train_cleaned.xml'

with open(file_path, 'r', encoding='utf-8') as file:
    xml_content = file.read()

print('file open')

parser = XmlParser()
questions = parser.parse(file_path, NlmQuestions)

print('parsed')

print(json.dumps(questions, default=lambda o: o.__dict__))

with open('data/json/train_cleaned.json', 'w') as archivo:
    json.dump(questions, archivo, default=lambda o: o.__dict__, indent=4)

"""


print('parsed')

# Print the parsed data
print(nlm_question)

print('parsed printed')

# Convert to a dictionary for easier DataFrame conversion
data_dict = {
    "questionid": nlm_question.questionid,
    "fRef": nlm_question.fRef,
    "subject": nlm_question.subject,
    "message": nlm_question.message,
    "sub_questions": [
        {
            "subqid": subq.subqid,
            "focus": subq.annotations.focus,
            "type": subq.annotations.type,
            "answers": [
                {
                    "answerid": ans.answerid,
                    "pairid": ans.pairid,
                    "content": ans.content
                } for ans in subq.answers
            ]
        } for subq in nlm_question.sub_questions.sub_questions
    ]
}

print('to dic')



# Flatten the sub_questions and answers to create a DataFrame
df = pd.json_normalize(data_dict, 
                        record_path=['sub_questions', 'answers'], 
                        meta=['questionid', 'fRef', 'subject', 'message', 
                            ['sub_questions', 'subqid'], 
                            ['sub_questions', 'focus'], 
                            ['sub_questions', 'type']],
                        errors='ignore')

print('to df')

df.to_csv('data/csv/train_dataset/CSV_Medical_Train_1.xml')

+




"""







