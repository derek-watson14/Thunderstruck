# # https://www.youtube.com/watch?v=OcD52lXq0e8
# # https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/
# # https://flask.palletsprojects.com/en/2.1.x/testing/

import pytest
import sys
sys.path.append('/Users/Jess/Documents/Software Design Class/project/Thunderstruck/flashcardz_app')
from flashcardz_app import create_app, db
from flashcardz_app.models import User, db
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Create globally accessible instances of important libaries
login_manager = LoginManager()
db = SQLAlchemy()

# Instantiate a Test Version of the App
@pytest.fixture()
def app():
    app = create_app()
    app.app_context().push()
    app.config.update({
        "TESTING": True,
        "WTF_CSRF_ENABLED": False
    })

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

# Instantiate an instance of a User
# Scope of module means run once per module (test file)
@pytest.fixture(scope='module')
def new_user():
    user = User(
        email='cool@test.edu'
    )
    user.set_password('testpassword')
    db.session.add(user)
    db.session.commit()
    return user
