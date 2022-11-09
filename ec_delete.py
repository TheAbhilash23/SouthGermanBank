import requests
import json


URL = 'http://127.0.0.1:8000/api/editdb/'
def delete_data():
    
    data = {
        'custid': 1000,
    }

    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)

    data = r.json()
    print(data)



delete_data()