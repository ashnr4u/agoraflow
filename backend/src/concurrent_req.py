import requests
from concurrent.futures import ThreadPoolExecutor

URL = "http://127.0.0.1:8000/register"

#for auth
token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0MiIsImlhdCI6MTc5MDg5MzMyMywiZXhwIjoxNzkwODk1MTIzfQ.YSKwb6UZi_hHQedjnfG_ypjTnmwHDsUKUu0pfyLAUCw"
event_id=8

headers= {
    "Authorization" : f"Bearer {token}",
    "Idempotency-key" : "1222"

}

'''
Define a function called send_request.
Inside it, use requests.post().
Send the request to your URL.
Include the event_id as the JSON body.
Include your headers.
Return the response status code and response body.
'''

def send_request():
    response= requests.post(url=URL, 
                            json={"event_id": event_id} ,
                            headers=headers
                            )
    return response.status_code ,response.text

with ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(lambda _: send_request(), range(2)))

print(results)