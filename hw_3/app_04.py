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

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from .forms_register import RegistrationForm
from .models_users import db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hw_4_database.db'
db.init_app(app)

app.config['SECRET_KEY'] = b'083f303cc0dad7507ec3fab7d2895c43334a4ccf56b19da628c4d90be9f03a09'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hi!'


@app.cli.command('init-db')
def init_db():
    db.create_all()


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(name=name, email=email).first()
        if user:
            return 'Такой пользователь уже есть!'
        else:
            new_user = User(name=name, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return 'Пользователь успешно зарегистрирован'
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
