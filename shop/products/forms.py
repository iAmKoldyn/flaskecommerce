from wtforms import Form, SubmitField, IntegerField, FloatField, StringField, TextAreaField, validators
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_babel import gettext
from flask_babel import _ 


class Addproducts(Form):
    name = StringField(gettext('Название'), [validators.DataRequired()])
    price = FloatField(gettext('Цена'), [validators.DataRequired()])
    discount = IntegerField(gettext('Скидка'), default=0)
    stock = IntegerField(gettext('Кол-во'), [validators.DataRequired()])
    size = IntegerField(gettext('Размер'), [validators.DataRequired()])
    colors = StringField(gettext('Цвет'), [validators.DataRequired()])
    discription = TextAreaField(gettext('Описание'), [validators.DataRequired()])
    gender = StringField(gettext('Гендер'), [validators.DataRequired()])
    image_1 = FileField('Image 1',
                        validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg']), gettext('Только изображение')])
    image_2 = FileField('Image 2',
                        validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg']), gettext('Только изображение')])
    image_3 = FileField('Image 3',
                        validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg']), gettext('Только изображение')])
