from flask import Flask, jsonify, request

from joblib import load

import pandas as pd

import os
import sys

import json

import logging

from config import MODEL_PATH

# set logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# set format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#for stream logs
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# add the stream handler
logger.addHandler(stream_handler)

app = Flask(__name__)


"""Routes"""
@app.route('/')
def index():

    # return jsonify({'results':'ok'}),200
    return "Welcome!"


@app.route('/v1/model/predict',methods=['POST'])
def predict():

    if request.method =='POST':
        json_data = request.get_json()
        logger.info(f'User input: {json_data}')

        logger.info('model being loaded....')
        # load the model
        try:
            loaded_model = load(MODEL_PATH)
            logger.info('model is loaded...')
            df = pd.DataFrame.from_dict([json_data])
            logger.info(f' columns: {df.columns}',file=sys.stderr)
            preds = loaded_model.predict(df)
            logger.info(f'predicted value: {preds[0]}')
            return jsonify({'prediction':preds[0]*1.0}),200
        except:
            logger.exception('Error in getting the result!!')

        

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)