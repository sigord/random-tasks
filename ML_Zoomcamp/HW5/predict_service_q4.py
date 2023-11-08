#!/usr/bin/env python
# coding: utf-8

import pickle

from flask import Flask
from flask import request
from flask import jsonify

THRESHOLD = 0.5

def load_pickle_file(filename: str):
    """
    Loads a pickle file.
    """
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)

dv = load_pickle_file('dv.bin')
model = load_pickle_file('model1.bin')

app = Flask('credit_scoring')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predicts the probability of a client 
    being solvent based on the client's data.
    """
    client = request.get_json()

    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    credit_solvent = y_pred > THRESHOLD

    result = {
        'credit_probability': float(round(y_pred, 3)),
        'credit_solvent': bool(credit_solvent)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
