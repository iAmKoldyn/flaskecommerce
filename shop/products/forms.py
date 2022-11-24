from wtforms import Form, SubmitField, IntegerField, FloatField, StringField, TextAreaField, validators
from flask_wtf.file import FileField, FileRequired, FileAllowed


class Addproducts(Form):
    name = StringField('Название', [validators.DataRequired()])
    price = FloatField('Цена', [validators.DataRequired()])
    discount = IntegerField('Скидка', default=0)
    stock = IntegerField('Кол-во', [validators.DataRequired()])
    colors = StringField('Цвет', [validators.DataRequired()])
    discription = TextAreaField('Описание', [validators.DataRequired()])

    image_1 = FileField('Image 1',
                        validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg']), 'Только изображение'])
    image_2 = FileField('Image 2',
                        validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg']), 'Только изображение'])
    image_3 = FileField('Image 3',
                        validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg']), 'Только изображение'])
