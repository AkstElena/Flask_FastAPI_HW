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
from random import randint

from flask import Flask, render_template
from .models_lib import db, Book, Author

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hw_database.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


@app.cli.command('init-db')
def init_db():
    db.create_all()


@app.cli.command("fill-db")
def fill_db():
    authors_dict = {'Терри Пратчетт': ['Стража! Стража!', 'Мрачный жрец', 'Роковая музыка', 'Цвет волшебства'],
                    'Умберто Эко': ['Имя розы', 'Маятник Фуко'],
                    'Робин Хобб': ['Королевский убийца', 'Волшебный корабль', 'Город драконов'],
                    'Нил Гейман': ['Американские боги', 'Звездная пыль'],
                    'Фредерик Бакман': ['Вторая жизнь Уве', 'Здесь была Бритт-Мари', 'Тревожные люди']}
    for el in authors_dict:
        new_author = Author(firstname=el.split()[0], lastname=el.split()[1])
        db.session.add(new_author)
    db.session.commit()
    for k, v in authors_dict.items():
        author = Author.query.filter_by(firstname=k.split()[0], lastname=k.split()[1]).first()
        for el in v:
            new_book = Book(name=el, year_publishing=1950 + randint(0, 60), count=randint(10, 101), id_author=author.id)
            db.session.add(new_book)
    db.session.commit()


@app.route('/books/')
def get_books():
    books = Book.query.all()
    context = {'books': books}
    return render_template('books.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
