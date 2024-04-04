"""
Задание №7
📌 Создайте форму регистрации пользователей в приложении Flask. Форма должна содержать поля: имя, фамилия, email,
пароль и подтверждение пароля. При отправке формы данные должны валидироваться на следующие условия:
○ Все поля обязательны для заполнения.
○ Поле email должно быть валидным email адресом.
○ Поле пароль должно содержать не менее 8 символов, включая хотя бы одну букву и одну цифру.
○ Поле подтверждения пароля должно совпадать с полем пароля.
○ Если данные формы не прошли валидацию, на странице должна быть выведена соответствующая ошибка.
○ Если данные формы прошли валидацию, на странице должно быть выведено сообщение об успешной регистрации.
"""

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from .forms_register_07 import RegistrationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = b'083f303cc0dad7507ec3fab7d2895c43334a4ccf56b19da628c4d90be9f03a09'
csrf = CSRFProtect(app)


@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        if not form.validate():
            flash(f'Данные некорретны!', 'danger')
        else:
            name = form.name.data
            flash(f'Пользователь {name} успешно зарегистрирован', 'success')
            return redirect(url_for('register'))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
