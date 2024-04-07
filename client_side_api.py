import requests

URL =  "http://127.0.0.1:8000/predict"
VALUES = [5.7,2.8,4.1,1.3]

data = {
    "values": VALUES
}

response = requests.post(URL, json=data)
if response.status_code == 200:
    data = response.json()
    print(data)