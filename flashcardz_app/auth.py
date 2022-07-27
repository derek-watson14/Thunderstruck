"""Routes for user authentication."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user

from . import login_manager
from .forms import LoginForm, RegistrationForm
from .models import User, db

# See this tutorial for more info on code: https://hackersandslackers.com/flask-login-user-authentication
# See this repo for sample code and file structure: https://github.com/toddbirchard/flasklogin-tutorial

# Blueprint Configuration
auth_bp = Blueprint(
    "auth_bp", __name__, template_folder="templates", static_folder="static"
)

@auth_bp.route('/register', methods = ['POST', 'GET'])
def register():
    """
        User registration page.
        GET requests serve sign-up page.
        POST requests validate form & user creation.
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        # Check that email isn't already in the DB
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            user = User(
                email = form.email.data
            )
            user.set_password(form.password1.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('main_bp.my_decks', email=user.email))

    return render_template("registration.html", form=form, title="Register")

@auth_bp.route('/', methods=['GET', 'POST'])
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
        Log-in page for registered users.
        GET requests serve Log-in page.
        POST requests validate and redirect user to dashboard.
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            flash("Logged in successfully " + user.email)
            return redirect(url_for('main_bp.my_decks', email=user.email))
        else:
            flash("Invalid username or password")
            return redirect(url_for("auth_bp.login"))

    return render_template('login.html', form=form, title="Login")


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in upon page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""

    flash("You must be logged in to view that page.")
    return redirect(url_for("auth_bp.login"))