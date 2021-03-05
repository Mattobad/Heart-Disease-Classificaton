import pytest

from flask import Flask

from app.app import create_app
from app.config import config


# test_dict = {"age":45, 
#             "sex":1, 
#             "cp":2, 
#             "trestbps":145,
#             "chol":235,
#             "fbs":0,
#             "restecg":0,
#             "thalach":180,
#             "exang":0,
#             "oldpeak":2.3,
#             "slope":0,
#             "ca":0,
#             "thal":1} 

@pytest.fixture()
def data_for_test():
    test_dict = {"age":45, 
            "sex":1, 
            "cp":1, 
            "trestbps":134,
            "chol":1,
            "fbs":134,
            "restecg":1,
            "thalach":120,
            "exang":1,
            "oldpeak":1.8,
            "slope":2,
            "ca":3,
            "thal":8} 

    yield test_dict



@pytest.fixture
def app():
    app = create_app(config_object=config.TestConfig)
    with app.app_context():
        yield app


@pytest.fixture()
def flask_test_client(app):
    with app.test_client() as test_client:
        yield test_client