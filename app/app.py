from flask import Flask, jsonify, request,render_template
from flask_cors import CORS

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
CORS(app)

"""Routes"""
@app.route('/')
def index():

    # return jsonify({'results':'ok'}),200
    return render_template('index.html'),200


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
        except:
            logger.exception('Error in loading model!!')

        try:
            df = pd.DataFrame.from_dict([json_data])
            logger.info(f'columns: {df.columns}')

        except:
            logger.exception('Error in converting into dataFrame')

        preds = loaded_model.predict(df)
        logger.info(f'predicted value: {preds[0]}')
        if preds==1:
            result = 'True'
        else:
            result = 'False'
        # converting to float as INT value is not json serializable
        return jsonify({'prediction':result}),200



        

if __name__ == '__main__':
    app.run(debug=True)