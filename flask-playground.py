"""
This module requests the flask application from the factory method in the app module. It also make visible a number of objects to the flask shell.
"""
import os
from dotenv import load_dotenv

app_root = os.path.dirname(__file__)

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# These imports are not located at the top of the file
# because none of the resources below can be initialized
# before the application is created. DO NOT CHANGE
from flask_migrate import Migrate, upgrade
from .app import create_app, db
# shell context dict entries definition
from .app.models import users_model


app = create_app('development')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=users_model.User)
