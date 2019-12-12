#super simple script just to send a reqest, you can use curl or whatever else you like as well

import requests

url = 'http://localhost:5000/predict'

r = requests.post(url, json={'Pregnancies': -0.844885,'Glucose': -1.206162,'BloodPressure': -0.529859,'SkinThickness': -0.012301,'Insulin': -0.181541,'BMI': -0.852200,'DiabetesPedigreeFunction': -0.365061,'Age': -0.190672})

print(r.json())

#0.639947, 0.865108, -0.033518, 0.670643, -0.181541, 0.166619, 0.468492, 1.425995
#-0.844885, -1.206162, -0.529859, -0.012301, -0.181541, -0.852200, -0.365061, -0.190672
#1.233880, 2.015813, -0.695306, -0.012301, -0.181541, -1.332500, 0.604397, -0.105584
#-0.844885, -1.074652, -0.529859, -0.695245, -0.540642, -0.633881, -0.920763, -1.041549	
#-1.141852, 0.503458, -2.680669, 0.670643, 0.316566, 1.549303, 5.484909, -0.020496