import requests
import json

headers = {
    'HTTP-X-PARTNER-AUTH': 'site-name:api-key',
    'Content-Type' : 'application/json',
}

url = 'https://api.periscopedata.com/api/v1/roles/0000-test-1111-role-id?test_mode=true'

response = requests.delete(url, headers=headers)

print(response.status_code)