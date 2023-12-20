import requests

req_f1 = requests.get(url='http://127.0.0.1:5000/api/flow/f1')
req_f2 = requests.get(url='http://127.0.0.1:5000/api/flow/f2')
dif = req_f1.json()[-1]['value']-req_f2.json()[-1]['value'] 
print(req_f1.json()[-1])
print(req_f2.json()[-1])

if dif < 0.9 :
    print("No leak") 
else:
    print("Leak Detected")