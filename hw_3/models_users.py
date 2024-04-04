"""
Задание №4
📌 Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна содержать следующие поля:
○ Имя пользователя (обязательное поле)
○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
📌 После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite) и выводиться сообщение
об успешной регистрации. Если какое-то из обязательных полей не заполнено или данные не прошли валидацию, то должно
выводиться соответствующее сообщение об ошибке.
📌 Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в базе данных. Если такой
пользователь уже зарегистрирован, то должно выводиться сообщение об ошибке.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Пользователь: {self.name}, e-mail: {self.email})'
