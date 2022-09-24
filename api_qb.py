from typing import Union    # python users version 3.6 to 3.9
from fastapi import FastAPI

app = FastAPI()  # instance


# if you want to have several parameters:


@app.get('/v1/users/details/{userID}')
async def ger_user_id(userID: int, user_name: str, password: str, location: Union[str, None] = None):  # to check api
    item = {'Message': 'You are using API for user ID: {}'.format(userID),
            'ID Data Type': '{}'.format(type(userID)),
            'user_name': user_name,
            'password': password
            }
    if location:
        item.update({'location': location})     # this query is optional (didn't necessary to fill it)
    return item     # terminal: uvicorn api_qb:app --reload and check in http://127.0.0.1:8000/docs



