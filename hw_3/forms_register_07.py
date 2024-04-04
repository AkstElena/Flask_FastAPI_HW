"""
Задание №7
📌 Создайте форму регистрации пользователей в приложении Flask. Форма должна содержать поля: имя, фамилия, email,
пароль и подтверждение пароля. При отправке формы данные должны валидироваться на следующие условия:
○ Все поля обязательны для заполнения.
○ Поле email должно быть валидным email адресом.
○ Поле пароль должно содержать не менее 8 символов, включая хотя бы одну букву и одну цифру.
○ Поле подтверждения пароля должно совпадать с полем пароля.
○ Если данные формы не прошли валидацию, на странице должна быть выведена соответствующая ошибка.
○ Если данные формы прошли валидацию, на странице должно быть выведено сообщение об успешной регистрации.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError


def validate_password(form, field):
    if not any(char.isdigit() for char in field.data):
        raise ValidationError('Поле должно включать хотя бы одну цифру')
    elif not any(char.isalpha() for char in field.data):
        raise ValidationError('Поле должно включать хотя бы одну букву')


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8), validate_password])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
