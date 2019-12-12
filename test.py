import pickle
import numpy as np
import pandas as pd

#simple test script with some dummy data- csv should have scaled values
model = pickle.load(open('KNN_diabetes.pkl','rb'))

dummy_data = pd.read_csv("dummy.csv")

for i in range((dummy_data.shape[0])):
    # grab each row one at a time
    print(list(dummy_data.iloc[i,:]))
    result = model.predict([list(dummy_data.iloc[i, :])])
    print(result)
