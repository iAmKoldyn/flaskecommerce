from wtforms import Form, StringField, TextAreaField, PasswordField,SubmitField,validators, ValidationError
from flask_wtf.file import FileRequired,FileAllowed, FileField
from flask_wtf import FlaskForm
from .model import Register




class CustomerRegisterForm(FlaskForm):
    name = StringField('Имя: ')
    username = StringField('Логин: ', [validators.DataRequired()])
    email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Пароль: ', [validators.DataRequired(), validators.EqualTo('confirm', message=' Both password must match! ')])
    confirm = PasswordField('Повторите пароль: ', [validators.DataRequired()])
    country = StringField('Страна: ', [validators.DataRequired()])
    city = StringField('Город: ', [validators.DataRequired()])
    contact = StringField('Телефон: ', [validators.DataRequired()])
    address = StringField('Адресс: ', [validators.DataRequired()])
    zipcode = StringField('Почтовый индекс: ', [validators.DataRequired()])

    profile = FileField('Profile', validators=[FileAllowed(['jpg','png','jpeg','gif'], 'Только картинки')])
    submit = SubmitField('Регистрация')

    def validate_username(self, username):
        if Register.query.filter_by(username=username.data).first():
            raise ValidationError("Это имя пользователя уже занято!")
        
    def validate_email(self, email):
        if Register.query.filter_by(email=email.data).first():
            raise ValidationError("Аккаунт с такой почтой уже существует!")

    


class CustomerLoginFrom(FlaskForm):
    email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Пароль: ', [validators.DataRequired()])