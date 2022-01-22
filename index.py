import requests
import json
import time

while True:
    response = requests.post('https://identity.fortellis.io/oauth2/aus1p1ixy7YL8cMq02p7/v1/token', data = {'grant_type':'client_credentials', 'scope':'anonymous'}, headers= {'Authorization':'Basic base64encoded{yourAPIKey:yourAPISecret}', 'Accept':'application/json', 'Cache-Control':'no-cache', })

    print(response.json())

    with open('currentToken.json', 'r+') as file:
        json.dump(response.json(), file, indent=2)
    time.sleep(10)