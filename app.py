import numpy as np
import pandas as pd
import pickle
from flask import  Flask, render_template, url_for, request, jsonify
from flask_cors import cross_origin

app = Flask(__name__, template_folder="template")
model = pickle.load(open("stroke.pkl", "rb"))
st = pd.read_csv("CStroke.csv")

@app.route("/", methods=['GET'])
@cross_origin()
def index():
    return render_template("index.html")


@app.route('/predict', methods=['GET','POST'])
@cross_origin()
def predict():
    if request.method ==  'POST':
        Gender = request.form['Gender']
        Age = request.form['Age']
        Hypertension = request.form['Hypertension']
        Heartdisease = request.form['Heartdisease']
        Married = request.form['Married']
        Work = (request.form['Work'])
        Residence = request.form['Residence']
        Glucose = (request.form['Glucose'])
        Bmi = (request.form['Bmi'])
        Smoking = (request.form['Smoking'])

        if (Gender == "Female"):
            Gender=0
        elif (Gender == "Male"):
            Gender=1
        else:
            Gender=2

        if (Hypertension == "No"):
             Hypertension = 0
        else:
             Hypertension = 1
        
        if (Heartdisease == "No"):
             Heartdisease = 0
        else:
             Heartdisease = 1

        if (Married == "No"):
             Married = 0
        else:
             Married = 1
        
        if (Work == "Govt_job"):
            Work = 0
        elif (Work == "Never_worked"):
            Work = 1
        elif (Work == "Private"):
            Work = 2
        elif (Work == "Self-employed"):
            Work = 3
        else:
            Work = 4

        if (Residence == "Rural"):
             Residence = 0
        else:
             Residence = 1
        
        if (Smoking == "Unknown"):
            Smoking = 0
        elif (Smoking == "formerly smoked"):
            Smoking = 1
        elif (Smoking == "never smoked"):
            Smoking = 2
        else:
            Smoking = 3


        prediction = model.predict(pd.DataFrame([[Gender,Age,Hypertension,Heartdisease,Married,Work,Residence,Glucose,Bmi,Smoking]], columns=['gender','age','hypertension','heartdisease','maritalstatus','worktype','Residencetype','glucoselevel','bmi','smokingstatus']))

        if(prediction== 0):
            prediction="You are keeping healthy, Congratuation!!!"
        else:
            prediction="You might have a Chance of stroke, Contact your doctor immediately!!"

        return render_template('index.html', prediction_text = 'Your Result is : {}'.format(prediction))
        
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)