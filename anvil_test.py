#Web UI: https://5ILJ4H4SE7QJB4W6.anvil.app/4KF24KONIOSDXXBLXZQXDKBC

import pickle
import numpy as np
import pandas as pd
import anvil.server
import anvil.media

#simple test script with some dummy data- csv should have scaled values
model = pickle.load(open('KNN_diabetes.pkl','rb'))

@anvil.server.callable
def show_result(file):
    with anvil.media.TempFile(file) as filename:
        diabetes_data = pd.read_csv(filename)
    
    result = []

    for i in range((diabetes_data.shape[0])):
        # grab each row one at a time
        row = model.predict([list(diabetes_data.iloc[i, :])])
        result.append(row[0])

    return(result)

anvil.server.connect("G7W7RMUBMZEB77SGQFRJO3IG-5ILJ4H4SE7QJB4W6")
anvil.server.wait_forever()