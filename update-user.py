import requests
import json

headers = {
    'HTTP-X-PARTNER-AUTH': 'site-name:api-key',
    'Content-Type' : 'application/json'
}

payload = {
    "first_name": 'newFirstName' ,
    "last_name": 'newLastName'
}

data = json.dumps(payload)

url = 'https://api.periscopedata.com/api/v2/users/0000-test-1111-user-id?test_mode=true'

response = requests.put(url, headers=headers, data=data)

print(json.loads(response.text))
