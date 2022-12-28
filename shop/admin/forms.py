from wtforms import BooleanField, StringField, PasswordField, validators, ValidationError
from flask_wtf import FlaskForm, Form
from .models import User
from flask_babel import gettext
from flask_babel import _ 


class RegistrationForm(FlaskForm):
    name = StringField(gettext('Имя'), [validators.Length(min=4, max=25)])
    username = StringField(gettext('Логин'), [validators.Length(min=4, max=25)])
    email = StringField(gettext('Email'), [validators.Length(min=6, max=35)])
    password = PasswordField(gettext('Пароль'), [
        validators.DataRequired(),
        validators.EqualTo('confirm', message=(gettext('Пароль должен содержать')))
    ])
    confirm = PasswordField(gettext('Повторите пароль'))

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(gettext('Такое имя пользователя уже существует.'))

        
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(gettext('Пользователь с такой почтой уже существует.'))
            

class LoginForm(FlaskForm):
    email = StringField('Email', [validators.Length(min=6, max=35)])
    password = PasswordField(gettext('Новый пароль'), [validators.DataRequired()])