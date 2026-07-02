from fastapi import FastAPI, Path, HTTPException, Query
import json

app=FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

        return data

@app.get('/')
def hello():
    return {'meassage': 'Patient management system API'}

@app.get('/about')
def about():
    return{'message': 'A fully functional API to patient records'}

@app.get('/view')
def view():
    data = load_data()

    return data

@app.get('/patient/{id}')
def view_patient(id: str=Path(..., description='id of the patient in the DB', examples='P001')):
    data=load_data()

    if id in data:
        return data[id]
    raise HTTPException(status_code=404, detail='Patient not found')

@app.get('/sort')
def sort_patients(sort_by: str= Query(...,description='sort on the basis of age,gender or bmi'),order: str=Query('asc', description='sort in asc or desc order')):
    valid_fields=['age','gender','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Invalid order select between asc and code')
    
    data=load_data()

    sort_order = True if order == 'desc' else False
    # print(f"DEBUG: First item type is {type(list(data.values())[0])}")
    # print(f"DEBUG: Data content: {list(data.values())[0]}")
    patients_list = data.get("patients", []) 

    sorted_data = sorted(
    patients_list, 
    key=lambda x: x.get(sort_by, 0), 
    reverse=sort_order
    )
    return sorted_data