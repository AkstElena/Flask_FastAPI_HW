"""
Задание №8
📌 Создать форму для регистрации пользователей на сайте.
📌 Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
📌 При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Пользователь: {self.firstname} {self.lastname}, e-mail: {self.email})'
