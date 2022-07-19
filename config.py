from os import environ, path

# If in development, use .env file
# If in production, heroku handles config variables in the apps
if environ.get("development"):
    from dotenv import load_dotenv

    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, ".env"))

class Config:
    """ 
    
    Set Flask Configuration variables from .env file
    
    All environmental variables should be stored in a .env file
    But .env files should not be included in the repo to protect secret keys and other info
    So the .gitignore file includes .env
    In the root level of this repo there is a `.env.example` file
    That file contains all of the variables referenced here in our configuration
    Copy the contents of that file to a file simple called `.env`, and change values as necessary
    Must have python package dotenv installed using:
    pip install python-dotenv
    
    """

    # General Config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")

    # Static Assest Config
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')

    # Database Config
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


