from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title='Name of the Patient', description='Give the name of the patient in less than 50 chars', examples=['Abhishekk','namdev'])]
    email:EmailStr
    linkedin_url:AnyUrl
    age: int=Field(gt=0,lt=120)
    weight:Annotated[float,Field(gt=0,strict=True)]
    married: Annotated[bool,Field(default=None, description='is the patient married or not')]
    allergies:Annotated[Optional[List[str]],Field(default=None, max_length=5)]
    contact_details:Dict[str,str]

def update_patient_date(patient:Patient):
    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Allergies: {patient.allergies}")
    print(f"Married: {patient.married}")
    print('--- Profile Updated ---')

patient_info = {'name':'abhishek', 'email':'ak@gmail.com','linkedin_url':'http://linkedin.com/123','age':'24', 'weight':'55.0','contact_details':{'phone':'12345'}}

patient1=Patient(**patient_info)

update_patient_date(patient1)
