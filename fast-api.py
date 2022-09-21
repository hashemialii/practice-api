from fastapi import FastAPI
from enum import Enum

app = FastAPI()  # instance


# the user can only use this models:
class Models(str, Enum):  # enumeration
    vggnet = 'vggnet'
    resnet = 'resnet'
    alexnet = 'alexnet'
    googlenet = 'googlenet'
    lemt = 'lent'


# To write api we need : method/path/function

@app.get('/')
async def root():
    return {'Message': 'Welcome to Dayche Class'}


# for create first api u should write on your terminal:
# uvicorn fast-api:app --reload (fast-api = the name of your folder in Python)
# next you can see return your function on web (http://127.0.0.1:8000)


@app.get('/v1/users/')
async def show_users():
    return {'Message': 'You are viewing user handling APIs'}


# next you can see return your function on web (http://127.0.0.1:8000/v1/users/)


# if you want to have parameter:

@app.get('/v1/users/{userID}')
async def ger_user_id(userID: int):  # annotation == type validation
    return {'Message': 'You are using API for user ID: {}'.format(userID),
            'ID Data Type': '{}'.format(type(userID))}

# now open http://127.0.0.1:8000/docs#/ and set parameter for checking
# or search http://127.0.0.1:8000/v1/users/2


@app.get('/v1/Models/{model_name}')
async def specify_model(model_name: Models):
    if model_name.value == 'vggnet':
        return {'model name': model_name,
                'Message': 'You are using API for model: {}'.format(model_name)}
    if model_name.value == 'resnet':
        return {'model name': model_name,
                'Message': 'You are using API for model: {}'.format(model_name)}
    if model_name.value == 'alexnet':
        return {'model name': model_name,
                'Message': 'You are using API for model: {}'.format(model_name)}
    if model_name.value == 'googlenet':
        return {'model name': model_name,
                'Message': 'You are using API for model: {}'.format(model_name)}
    if model_name.value == 'lemt':
        return {'model name': model_name,
                'Message': 'You are using API for model: {}'.format(model_name)}


# you can check it on http://127.0.0.1:8000/docs (to add option)






