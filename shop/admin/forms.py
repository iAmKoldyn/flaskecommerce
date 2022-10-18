from wtforms import BooleanField, StringField, PasswordField, validators , ValidationError
from flask_wtf import FlaskForm, Form
from .models import User


class RegistrationForm(FlaskForm):
    name = StringField('Имя', [validators.Length(min=4, max=25)])
    username = StringField('Логинme', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=35)])
    password = PasswordField('Пароль', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Пароль должен содержать')
    ])
    confirm = PasswordField('Повторите пароль')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Такое имя пользователя уже существует.')

        
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Пользователь с такой почтой уже существует.')
            

class LoginForm(FlaskForm):
    email = StringField('Email', [validators.Length(min=6, max=35)])
    password = PasswordField('Новый пароль', [validators.DataRequired()])