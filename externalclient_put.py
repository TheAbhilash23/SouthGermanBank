import requests
import json


URL = 'http://127.0.0.1:8000/api/editdb/'
def update_db():
    data = {
        'custid': 0,
        'age': 99,
        'other_installment_plans': 3,
        'housing': 1,
        'number_credits': 1,
        'job': 3,
        'people_liable': 1,
        'telephone': 2,
        'foreign_worker': 2,

    }

    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)

    data = r.json()
    print(data)
    
update_db()






# custid 0 ki age 21 hai