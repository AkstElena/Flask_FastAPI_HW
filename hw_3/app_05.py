"""
Задание №5
📌 Создать форму регистрации для пользователя.
📌 Форма должна содержать поля: имя, электронная почта, пароль (с подтверждением), дата рождения, согласие на
обработку персональных данных.
📌 Валидация должна проверять, что все поля заполнены корректно (например, дата рождения должна быть в
формате дд.мм.гггг).
📌 При успешной регистрации пользователь должен быть перенаправлен на страницу подтверждения регистрации.
"""

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from .forms_register_BD import RegistrationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = b'083f303cc0dad7507ec3fab7d2895c43334a4ccf56b19da628c4d90be9f03a09'
csrf = CSRFProtect(app)



@app.route('/', methods=['GET', 'POST'])
def register_bd():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        date_of_birth = form.date_of_birth.data
        print(name, email, password, date_of_birth)
        return render_template('hello.html', name=name)
    return render_template('register_DB.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
