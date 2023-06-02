import requests
import json

def facts(): 
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': 's1c8N5QKSo6KEa7wChT4uA==OLH22E3Avonlofw6'})
    if response.status_code == requests.codes.ok:
        return response.json()  # Parse the JSON response into a Python dictionary
    else:
        print("Error:", response.status_code, response.text)
        return None

# a = facts()
# if a:
#     print(a[0]['fact'])  # Access the fact directly from the dictionary