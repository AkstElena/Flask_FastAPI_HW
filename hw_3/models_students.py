"""
📌 Доработаем задача про студентов
📌 Создать базу данных для хранения информации о студентах и их оценках в учебном заведении.
📌 База данных должна содержать две таблицы: "Студенты" и "Оценки".
📌 В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
📌 В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
📌 Необходимо создать связь между таблицами "Студенты" и "Оценки".
📌 Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их оценок.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    group = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(50))
    id_faculty = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)
    grade = db.relationship('Grade', backref=db.backref('student'), lazy=True)

    def __repr__(self):
        return f'Студент: {self.firstname} {self.lastname}, {self.faculty}, {self.grade})'


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    student = db.relationship('Student', backref=db.backref('faculty'), lazy=True)

    def __repr__(self):
        return f'{self.name}'


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_student = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    lesson = db.Column(db.String(30), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Оценка по дисциплине {self.lesson}: {self.score}'
