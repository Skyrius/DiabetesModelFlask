#super simple script just to send a reqest, you can use curl or whatever else you like as well

import requests

url = 'http://localhost:5000/predict'

r = requests.post(url, json={'Pregnancies': 0.639947,'Glucose': 0.865108,'BloodPressure': -0.033518,'SkinThickness': 0.670643,'Insulin': -0.181541,'BMI': 0.166619,'DiabetesPedigreeFunction': 0.468492,'Age': 1.425995})

print(r.json())