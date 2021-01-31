import json
# from config import test_dict
from app import index

from pathlib import Path

#root package 


def test_index():
    assert index() ==  "Welcome!"


# def test_health_endpoint_returns_200(flask_test_client):

#     # when
#     res = flask_test_client.get('/')

#     # then
#     assert res.status_code ==200


# def test_pred_endpoint_returns_prediciton(flask_test_client):

#     #when 
#     response = flask_test_client.post('/v1/predict/model',json=test_dict)

#     #then
#     assert response.status_code == 200

#     response_json = json.loads(response.data)
#     prediction = response_json['prediction']

#     assert type(prediction) is float