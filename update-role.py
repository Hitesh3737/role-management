import requests
import json

headers = {
    'HTTP-X-PARTNER-AUTH': 'site-name:api-key',
    'Content-Type' : 'application/json'
}

payload =  {
            "name": "myExistingRole" ,
            "description": "NewDescription",
            "updated_by_email": "useremail@website.com"
}

data = json.dumps(payload)

url = 'https://api.periscopedata.com/api/v1/roles/0000-test-1111-role-id?test_mode=true'

response = requests.put(url, headers=headers, data=data)