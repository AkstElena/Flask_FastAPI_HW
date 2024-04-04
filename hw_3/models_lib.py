"""
Задание №2
📌 Создать базу данных для хранения информации о книгах в библиотеке.
📌 База данных должна содержать две таблицы: "Книги" и "Авторы".
📌 В таблице "Книги" должны быть следующие поля: id, название, год издания,
количество экземпляров и id автора.
📌 В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
📌 Необходимо создать связь между таблицами "Книги" и "Авторы".
📌 Написать функцию-обработчик, которая будет выводить список всех книг с
указанием их авторов.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    year_publishing = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    id_author = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __repr__(self):
        return f'Книга "{self.name}" {self.author}'


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    book = db.relationship('Book', backref=db.backref('author'), lazy=True)

    def __repr__(self):
        return f'Автор: {self.firstname} {self.lastname}'


