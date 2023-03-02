from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .views import main_views

import config

app = Flask(__name__)
app.register_blueprint(main_views.bp)

# db = SQLAlchemy()
# migrate = Migrate()


# def craete_app():
#     app=Flask(__name__)
#     app.config.from_object(config)

#     # ORM
#     db.init_app(app)
#     migrate.init_app(app, db)

#     # blueprint
#     app.register_blueprint(main_views.bp)

#     return app
