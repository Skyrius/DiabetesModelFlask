from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
#import pandas as pd

app = Flask(__name__)

# for POST, you can change it to any other protocol as needed
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            #Get request from json- it should be in the form 
            #json = {'Pregnancies': ,'Glucose': ,'BloodPressure': ,'SkinThickness': ,
            # 'Insulin': ,'BMI': ,'DiabetesPedigreeFunction' ,'Age': }

            #also note, because the model was trained on scaled data the input also has to be scaled
            # ## Scaling the data 
            # data Z is rescaled such that μ = 0 and 𝛔 = 1, and is done through this formula:
            # ![](https://cdn-images-1.medium.com/max/800/0*PXGPVYIxyI_IEHP7.)
            # 
            # 
            # #### to learn more about scaling techniques
            # https://medium.com/@rrfd/standardize-or-normalize-examples-in-python-e3f174b65dfc
            # https://machinelearningmastery.com/rescaling-data-for-machine-learning-in-python-with-scikit-learn/
            
            diabetes_data = request.get_json()

            #If for some reason we're uploading multiple inputs as a csv, there's a dummy html just to upload
            #you'd still need to parse the results but it's here
            #diabetes_data = pd.read_csv(request.files.get('file'))
            
            diabetes_data_input = [[diabetes_data['Pregnancies'],diabetes_data['Glucose'],diabetes_data['BloodPressure'],diabetes_data['SkinThickness'],diabetes_data['Insulin'],diabetes_data['BMI'],diabetes_data['DiabetesPedigreeFunction'],diabetes_data['Age']]]

            #load model
            model = pickle.load(open('KNN_diabetes.pkl','rb'))
            result = model.predict(diabetes_data_input)

        except ValueError:
            return jsonify("Invalid input format")

        return jsonify(result.tolist())

        #if you're using html to upload a csv you can use this
        #return render_template('upload.html', result=model.predict(result))


if __name__ == '__main__':
    app.run(debug=True)