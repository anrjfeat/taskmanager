import requests
import json

URL='http://127.0.0.1:8000/task/new/'

data = {
    "name":"Maths assignment",
    "description":"Complete todays assignment",
    "email":"user@example.com"
    }

json_data=json.dumps(data)
r=requests.post(url=URL,data=json_data)
data=r.json()
print(data)