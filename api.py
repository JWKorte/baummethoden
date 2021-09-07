from flask import Flask, Response, request
import pandas as pd
from werkzeug.utils import bind_arguments
from flask_cors import CORS
import os
from io import StringIO

app = Flask(__name__)
CORS(app)

training_data = pd.read_csv(os.path.join("auto-mpg.csv"))

trained_model = pd.read_pickle(os.path.join("models", "baummethoden.pickle"))

prediction_data = pd.read_csv(os.path.join("prediction_input_mpg.csv"))

@app.route("/")
def main():
    return {"hello":"world"}

@app.route("/training_data")
def get_training_data():
    return Response(training_data.to_json(), mimetype="application/json")

@app.route("/prediction_data")
def get_prediction_data():
    return Response(prediction_data.to_json(), mimetype="application/json")

@app.route("/predict")
def predict():
    zylinder = request.args.get('zylinder')
    ps = request.args.get("ps")
    gewicht = request.args.get("gewicht")
    beschleunigung = request.args.get("beschleunigung")
    baujahr = request.args.get("baujahr")
    data=[[float(zylinder),float(ps),float(gewicht),float(beschleunigung),float(baujahr)]]
    #csv_string = (",".join([zylinder,ps,gewicht,beschleunigung,baujahr]))
    result = trained_model.predict(data)
    return {"result":result[0]}
    
if __name__ == "__main__":
    app.run()