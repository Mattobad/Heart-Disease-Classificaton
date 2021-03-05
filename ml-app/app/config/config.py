import os 
from pathlib import Path


# root package
PACKAGE_NAME = Path().resolve()

MODEL_NAME = 'clf_heart_disease.sav'
MODEL_PATH_INNER = os.path.join("app",'trained-model')
MODEL_PATH = PACKAGE_NAME / MODEL_PATH_INNER



test_dict = {"age":45, 
            "sex":1, 
            "cp":2, 
            "trestbps":145,
            "chol":235,
            "fbs":0,
            "restecg":0,
            "thalach":180,
            "exang":0,
            "oldpeak":2.3,
            "slope":0,
            "ca":0,
            "thal":1} 

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'things-to-keep-secret'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestConfig(Config):
    TESTING = True