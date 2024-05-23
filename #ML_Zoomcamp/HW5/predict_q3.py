#!/usr/bin/env python
# coding: utf-8

import pickle
import logging

# set up logging only to console
logging.basicConfig(level=logging.INFO, format='%(message)s')

model_file = 'model1.bin'
dv_file = 'dv.bin'


with open(model_file, 'rb') as f_in:
    logging.info('Loading the model...')    
    model = pickle.load(f_in)
    
with open(dv_file, 'rb') as f_in:
    logging.info('Loading the dv...')
    dv = pickle.load(f_in)
    
client = {"job": "retired", "duration": 445, "poutcome": "success"}


def predict(client, dv, model):
    logging.info('Predicting...')
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    return y_pred


if __name__ == "__main__":
    print(round(predict(client, dv, model), 3))


