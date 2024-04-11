import requests
import json

headers = {
    'HTTP-X-PARTNER-AUTH': 'site-name:api-key',
    'Content-Type' : 'application/json'
}

payload = {
    "name": "myNewRole" ,
    "description": "testing",
    "created_by_email": "useremail@website.com",
    "privileges":
    [{
            "object_type":"Dashboard",
            "permissions":["read_dashboards"]
        }]
    ,
    "permissions":
    [{
        "object_type":"Dashboard",
        "object_id":"0000-dashboard-1111-id",
        "permissions":["create_dashboards"]
                       }]
}

data = json.dumps(payload)

url = 'https://api.periscopedata.com/api/v1/roles?test_mode=true'

response = requests.post(url, headers=headers, data=data)

print(json.loads(response.text))