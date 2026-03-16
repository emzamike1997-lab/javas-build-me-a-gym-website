```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import DevelopmentConfig
from routes import main as main_blueprint

db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_class=DevelopmentConfig):
    """Create the Flask application"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    jwt.init_app(app)
    app.register_blueprint(main_blueprint)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
```

###