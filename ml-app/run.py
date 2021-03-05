from app.app import  create_app
from app.config import config


if __name__ == '__main__':
    app = create_app(config_object=config.DevelopmentConfig)
    app.run(debug=True)