from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

with open('house_price_prediction.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [
        float(request.form['CRIM']),
        float(request.form['ZN']),
        float(request.form['INDUS']),
        float(request.form['CHAS']),
        float(request.form['NOX']),
        float(request.form['AGE']),
        float(request.form['DIS']),
        float(request.form['PTRATIO']),
        float(request.form['B']),
        float(request.form['LSTAT'])
    ]
features array np.array([features])
prediction = model.predict(features_array)
output = round (prediction[0],2)
return render_template("index.html", prediction text-f"predicted Price: (output)")
if _name_== "_main_":
     app.run(debug=True)

