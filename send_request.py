# send_request.py
import requests

url = "http://127.0.0.1:8000/largest_rectangle"
headers = {"Content-Type": "application/json"}
data = {"matrix": [[1,1,1,0,1,-9],[1,1,1,1,2,-9],[1,1,1,1,2,-9],[1,0,0,0,5,-9],[5,0,0,0,5]]}

response = requests.post(url, headers=headers, json=data)
print(response.json())
