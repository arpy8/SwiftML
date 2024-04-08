import requests

URL =  "http://127.0.0.1:8000/predict"
MODEL_ID = "972dcd4f5a67a701ebe6bb579f50c69a165d734caf3c60c492a048e543bda9b6"
VALUES = [19.56,9.17,0.61,1629.95,1270.17,343.44,0.28,406.96,0.53,296.99,569.73,7.0,183.84,237.23,79.52,51.3,3.32]

data = {
    "model_id": MODEL_ID,
    "values": VALUES
}

response = requests.post(URL, json=data)

if response.status_code == 200:
    data = response.json()
    print(data)
    
print(response)