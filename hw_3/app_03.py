"""
Задание №3
📌 Доработаем задача про студентов
📌 Создать базу данных для хранения информации о студентах и их оценках в учебном заведении.
📌 База данных должна содержать две таблицы: "Студенты" и "Оценки".
📌 В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
📌 В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
📌 Необходимо создать связь между таблицами "Студенты" и "Оценки".
📌 Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их оценок.
"""
import random
from random import randint

from flask import Flask, render_template
from .models_students import db, Student, Faculty, Grade

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hw_3_database.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


@app.cli.command('init-db')
def init_db():
    db.create_all()


@app.cli.command("fill-db")
def fill_db():
    for faculty in ['автомеханический', 'юридический', 'экономический']:
        new_faculty = Faculty(name=f'Факультет {faculty}')
        db.session.add(new_faculty)
    db.session.commit()
    for _ in range(10):
        firstname = random.choice(['Юрий', 'Алексей', 'Марк', 'Антон', 'Александр', 'Игорь', 'Матвей'])
        lastname = random.choice(['Иванов', 'Петров', 'Сидоров', 'Королев'])
        group = random.choice(['2201a', '5125п', '2311д'])
        new_student = Student(firstname=firstname, lastname=lastname, email=firstname + lastname + '@mail.ru',
                              group=group, id_faculty=randint(1, 3))
        db.session.add(new_student)
    db.session.commit()
    for i in range(10):
        for lesson in ['Высшая математика', 'История России', 'Экономика', 'Психология и педагогика']:
            new_grade = Grade(lesson=lesson, score=randint(2, 5), id_student=i + 1)
            db.session.add(new_grade)
    db.session.commit()


@app.route('/students/')
def get_students():
    students = Student.query.all()
    context = {'students': students}
    return render_template('students.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
