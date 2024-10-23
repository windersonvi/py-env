from fastapi import FastAPI, Response

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,4,5]

@app.get('/contact')
def get_contact():
    return {'name': 'PLATZI'}



