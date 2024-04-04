"""
Задание №5
📌 Создать форму регистрации для пользователя.
📌 Форма должна содержать поля: имя, электронная почта, пароль (с подтверждением), дата рождения, согласие на
обработку персональных данных.
📌 Валидация должна проверять, что все поля заполнены корректно (например, дата рождения должна быть в
формате дд.мм.гггг).
📌 При успешной регистрации пользователь должен быть перенаправлен на страницу подтверждения регистрации.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    email = StringField('Электронная почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=5, max=8)])
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')])
    date_of_birth = DateField('Дата рождения', format='%Y-%m-%d')
    agreement = BooleanField('Согласие на обработку персональных данных', default=False, validators=[DataRequired()])
