import json

def test_health_endpoint_returns_200(flask_test_client):

    # when
    res = flask_test_client.get('/health')

    # then
    assert res.status_code ==200

    res_json = json.loads(res.data)
    assert res_json['health'] == 'ok'


def test_pred_endpoint_returns_prediciton(flask_test_client,data_for_test):

    #when 
    response = flask_test_client.post('/v1/model/predict',json=data_for_test)

    #then
    assert response.status_code == 200

    response_json = json.loads(response.data)
    prediction = response_json['prediction']

    assert prediction in ['True','False']