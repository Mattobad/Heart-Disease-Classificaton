from flask import Blueprint, jsonify, request,render_template
from flask_cors import CORS

from joblib import load
import pandas as pd

import os
import sys
import json
import logging

from app.config import config

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

pred_app = Blueprint('pred_app',__name__)
CORS(pred_app)

"""Routes"""
@pred_app.route('/')
def index():

    # return 'ok'
    # return jsonify({'results':'ok'}),200
    return render_template('index.html'),200

@pred_app.route('/health')
def health_status():

    return jsonify({'health':'ok'}),200

@pred_app.route('/v1/model/predict',methods=['POST'])
def predict():

    if request.method =='POST':
        json_data = request.get_json()
        logger.info(f'User input: {json_data}')

        logger.info('model being loaded....')
        # load the model
        try:
            path = os.path.join(config.MODEL_PATH,config.MODEL_NAME)
            loaded_model = load(path)
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
