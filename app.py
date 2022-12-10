from flask import Flask,request,jsonify
import numpy as np
import pickle

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome To Income Prediction Page!"



@app.route('/income-predict',methods=['POST'])
def predict():

    REGION_TYPE = request.form.get('REGION_TYPE')
    GENDER = request.form.get('GENDER')
    AGE = request.form.get('AGE')
    EDUCATION = request.form.get('EDUCATION')
    OCCUPATION = request.form.get('OCCUPATION')
    MARITAL_STATUS = request.form.get('MARITAL_STATUS')

    input_query = np.array([[REGION_TYPE, GENDER, AGE, EDUCATION, OCCUPATION, MARITAL_STATUS]])

    result = model.predict(input_query)[0]

    return jsonify({'Income Prediction': str(result)})

if __name__ == '__main__':
    app.run(debug=True)