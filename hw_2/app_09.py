"""
Задание №9
📌 Создать страницу, на которой будет форма для ввода имени и электронной почты
📌 При отправке которой будет создан cookie файл с данными пользователя
📌 Также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
📌 На странице приветствия должна быть кнопка "Выйти"
📌 При нажатии на кнопку будет удален cookie файл с данными пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.
"""

from flask import Flask, request, render_template, redirect, url_for, flash, session, make_response

app = Flask(__name__)
app.secret_key = b'083f303cc0dad7507ec3fab7d2895c43334a4ccf56b19da628c4d90be9f03a09'


@app.route('/', methods=['GET', 'POST'])
def fill_form():
    if request.method == 'POST':
        if not request.form['name'] and not request.form['email']:
            flash('Необходимо ввести данные!', 'danger')
            return redirect(url_for('fill_form'))
        name = request.form.get('name')
        email = request.form.get('email')
        session['username'] = f'{name}&{email}'
        return redirect(url_for('hello', name=name))
    return render_template('login.html', title='Задача 9')


@app.route('/redirect/<name>')
def hello(name):
    return render_template('hello.html', name=name, title='Hello')


@app.route('/getsession/')
def get_session():
    return f"Значение session: {session['username']}"


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('fill_form'))


if __name__ == '__main__':
    app.run(debug=True)
