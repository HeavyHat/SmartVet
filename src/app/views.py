from app import app
from flask import render_template, request, redirect, abort, url_for
from flask_security import Security, SQLAlchemySessionUserDatastore, login_required, LoginForm, RegisterForm, url_for_security
from flask_security.forms import StringField, PasswordField, Required, Email, BooleanField
from models.database import db_session, init_db
from models.model import User, Role




class CustomLoginform(LoginForm):
    email = StringField('E-mail', validators=[Email()])
    password = PasswordField('Password', validators=[Required()])
    rememberMe = BooleanField('Remember Me')


class CustomRegisterform(RegisterForm):
    email = StringField('Email', validators=[Email(), Required()])
    password = PasswordField('Password', validators=[Required()])
    first_name = StringField('First Name', validators=[Required()])
    last_name = StringField('Last Name', validators=[Required()])
    practice = StringField('Veterinary Practice',  validators=[])
    location = StringField('Closest town or city to the practice',  validators=[])
    howDidYouHear = StringField('How did you hear about us?',  validators=[])
    agree = BooleanField('I agree with the terms and conditions which apply when using this product.',  validators=[])


init_db()
app.config.from_object('config.configurations.DevelopmentConfig')
print(" * Running with the following configuration: ")
for key, value in sorted(app.config.items()):
    print(" *   " + str(key) + " = " + str(value))
user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
security = Security(app, user_datastore, login_form=CustomLoginform, register_form=CustomRegisterform)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")


@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    return redirect(url_for('dashboard'))

@app.route('/unauthorised')
@app.errorhandler(403)
def unauthorised():
    return render_template("error_pages/403_page,html"), 403


@app.route('/not_found')
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error_pages/404_page.html'), 404
