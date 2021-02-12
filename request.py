import requests

url = 'http://localhost:5000/predict'
r = requests.post(url,json={'rank':2, 'sales_in_first_month':9, 'sales_in_second_month':6})

print(r.json())