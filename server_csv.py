from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        try:
            result = []
            #load model and read in data
            model = pickle.load(open('KNN_diabetes.pkl','rb'))
            diabetes_data = pd.read_csv(request.files.get('file'))

            for i in range((diabetes_data.shape[0])):
                # grab each row one at a time
                row = model.predict([list(diabetes_data.iloc[i, :])])
                result.append(row[0])

            listToStr = ' '.join([str(elem) for elem in result])
            return render_template('DiabetesPrediction.html', result_list="The result list is: ["+listToStr+"] (1 = diabetes, 0 = no diabetes)")

        except ValueError:
            return render_template("DiabetesPrediction.html", result_list="Invalid format")

    return render_template('DiabetesPrediction.html', result_list="")

if __name__ == '__main__':
    app.run(debug=True)