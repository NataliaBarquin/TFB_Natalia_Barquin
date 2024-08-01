from pydantic import BaseModel, Field
from pydantic_xml import BaseXmlModel, attr, element
from typing import List, Optional
import pandas as pd

class Answer(BaseXmlModel):
    answerid: str = attr(name="answerid")
    pairid: str = attr(name="pairid")
    content: str = element()

    class Config:
        tag = "ANSWER"

class Annotations(BaseXmlModel):
    focus: str = element(name="FOCUS")
    type: str = element(name="TYPE")

    class Config:
        tag = "ANNOTATIONS"

class SubQuestion(BaseXmlModel):
    subqid: str = attr(name="subqid")
    annotations: Annotations = element()
    answers: list[Answer] = element(tag="ANSWER", default_factory=list)

    class Config:
        tag = "SUB-QUESTION"

class SubQuestions(BaseXmlModel):
    sub_questions: list[SubQuestion] = element(tag="SUB-QUESTION", default_factory=list)

    class Config:
        tag = "SUB-QUESTIONS"

class NlmQuestion(BaseXmlModel):
    questionid: str = attr(name="questionid")
    fRef: str = attr(name="fRef")
    subject: str = element(name="SUBJECT")
    message: str = element(name="MESSAGE")
    sub_questions: SubQuestions = element()

    class Config:
        tag = "NLM-QUESTION"



class NLMQuestions(BaseXmlModel, tag = "NLM-QUESTIONS"):
    nlm_questions: List[NlmQuestion] = Field(alias="NLM-QUESTION")
        


# The XML string you want to parse
file_path = "data/xml/train_dataset/TREC-2017-LiveQA-Medical-Train-1.xml"

with open(file_path, 'r', encoding='utf-8') as file:
    xml_content = file.read()

print('file open')

# Parse the XML content into the NlmQuestion model
nlm_question = NLMQuestions.from_xml(xml_content)

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







