import requests
import json
import pandas as pd

#insert csv file that contains names and emails
df = pd.read_csv('user_data.csv')

#use get roles api call to get role id
roles = 'create-role.py'
invited = 'john@example.co'

#split first and last name if they are together in one column
df['last_name'] = df['Name'].str.split().str[1]
df['first_name'] = df['Name'].str.split().str[0]

#keep these variables blank
first_name = ''
last_name = ''
email = ''

#loop through each user in csv and create user
for index, row in df.iterrows():
    first_name = row['first_name']
    last_name = row['last_name']
    email = row['Email']

    #insert site name and api_key
    headers = {
        'HTTP-X-PARTNER-AUTH': 'site_name:api_key',
        'Content-Type' : 'application/json'
    }

    payload = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "roles": [
          roles
        ],
        "invited_by_email": invited
    }
    data = json.dumps(payload)
    #use test_mode=true to test script
    url = 'https://api.periscopedata.com/api/v2/users?test_mode=false'
    response = requests.post(url, headers=headers, data=data)
    print(payload)

print(json.loads(response.text)) 