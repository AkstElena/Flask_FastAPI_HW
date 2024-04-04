"""
Задание №6
📌 Дополняем прошлую задачу
📌 Создайте форму для регистрации пользователей в вашем веб-приложении.
📌 Форма должна содержать следующие поля: имя пользователя, электронная почта, пароль и подтверждение пароля.
📌 Все поля обязательны для заполнения, и электронная почта должна быть валидным адресом.
📌 После отправки формы, выведите успешное сообщение об успешной регистрации.
"""

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from .forms_register import RegistrationForm

app = Flask(__name__)


app.config['SECRET_KEY'] = b'083f303cc0dad7507ec3fab7d2895c43334a4ccf56b19da628c4d90be9f03a09'
csrf = CSRFProtect(app)


@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        flash(f'Пользователь {name} успешно зарегистрирован', 'success')
        return redirect(url_for('register'))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
