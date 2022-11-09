import requests
import json


URL='http://127.0.0.1:8000/api/editdb/'

data = {
    'custid':1000,
    'credit_risk':0,
    'status':1,
    'duration':30,
    'credit_history':2,
    'purpose':2,
    'amount':6350,
    'savings':4,
    'employment_duration':4,
    'installment_rate':3,
    'personal_status_sex':2,
    'other_debtors':2,
    'present_residence':8,
    'property_type':1,
    'age':33,
    'other_installment_plans':3,
    'housing':1,
    'number_credits':1,
    'job':3,
    'people_liable':1,
    'telephone':2,
    'foreign_worker':2,

}

json_data = json.dumps(data)
r = requests.post(url = URL, data = json_data)

data = r.json()
print(data)