import requests
import json

headers = {
    'HTTP-X-PARTNER-AUTH': 'site-name:api-key',
    'Content-Type' : 'application/json'
}

url = 'https://api.periscopedata.com/api/v1/roles'

response = requests.get(url, headers=headers)

print(json.loads(response.text))