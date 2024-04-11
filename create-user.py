import requests
import json

headers = {
    'HTTP-X-PARTNER-AUTH': 'site-name:api-key',
    'Content-Type' : 'application/json'
}

payload = {
    "first_name": 'MyFirstName' ,
    "last_name": 'MyLastName',
    "email": 'newuseremail@website.com',
    "roles": [
      '0000-admin-1111-id'
    ],
    "invited_by_email": 'useremail@website.com' }

data = json.dumps(payload)

url = 'https://api.periscopedata.com/api/v2/users?test_mode=true'

response = requests.post(url, headers=headers, data=data)

print(json.loads(response.text))
