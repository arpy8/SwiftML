import os
import json
import pickle
import numpy as np
import pandas as pd
# from pymongo import MongoClient
from termcolor import colored
from flask import Flask, request, jsonify, abort, render_template_string

# config
# MONGO_URL=os.environ.get("MONGO_URL")
AUTH_TOKEN = "test"
Model_Token = "0111234"

# client = MongoClient(MONGO_URL)
# db = client.get_database("lebon")
# records = db.count

# mongo functions
# def get_count():
#     return records.find_one({"total_hits": {"$exists": True}})["total_hits"]

# def increase_count():
#     curr_count = get_count()
#     try:
#         records.update_one({}, {"$set": {"total_hits": curr_count+1}})
#         return f"{curr_count+1}"
    
#     except Exception as e:
#         return f"Error: {e}"


# flask app

def load_params_and_model(key):
    if key == Model_Token:
        pickle_path = r"C:\Users\arpit\My_PC\repos\SwiftML\models\final_dumped_LinearDiscriminantAnalysis.pkl"
        
        with open(pickle_path, 'rb') as file:
            params, model = pickle.load(file)
    
        return params, model
        # def predict():
        #     classes = ['setosa', 'versicolor', 'virginica']
        #     ml_list = [1, 5.1, 3.5, 1.4, 0.2]
        #     ml = [1,3,'alfa-romero giulia','gas','std','two','convertible','rwd','front',88.6,168.8,64.1,48.8,2548,'dohc','four',130,'mpfi',3.47,2.68,9,111,5000,21,27]

        #     temp = pd.DataFrame([ml], columns=params)

        # return predict()

    else:
        return "False", "Invalid token"
        

app = Flask(__name__)

# @app.before_request
# def check_auth():
#     if request.endpoint == 'get_post_data':
#         token = request.headers.get('Authorization')
#         if token != AUTH_TOKEN:
#             abort(401, 'Unauthorized access >:(')

@app.route("/")
def index():
    return jsonify({"success": "Welcome to the test API for SwiftMl!"})

@app.route("/predict", methods=["POST"])
def get_post_data():
    # try:
        values = request.json.get("values")
        
        # return jsonify({"success": f"{values}"})
        
        if type(values) != list:
            return jsonify({"error": "Invalid request data"}), 400

        params, model = load_params_and_model(Model_Token)
        
        if params == "False":
            return jsonify({"error": model}), 401
        
        if len(values)!=len(params):
            return jsonify({"error": "Invalid number of features", "params":params}), 400
        
        data = pd.DataFrame([values], columns=params)   
        
        print(data)
        
        prediction = model.predict(data)
    
        return jsonify({"success": f"{prediction}"})

    # except Exception as e:
    #     print(e)
    #     return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)