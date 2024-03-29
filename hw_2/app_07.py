"""
Задание №7
📌 Создать страницу, на которой будет форма для ввода числа и кнопка "Отправить"
📌 При нажатии на кнопку будет произведено перенаправление на страницу с результатом, где будет выведено введенное
число и его квадрат.
"""

from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = b'083f303cc0dad7507ec3fab7d2895c43334a4ccf56b19da628c4d90be9f03a09'


@app.route('/', methods=['GET', 'POST'])
def fill_form():
    if request.method == 'POST':
        if not request.form['number']:
            flash('Необходимо ввести число!', 'danger')
            return redirect(url_for('fill_form'))
        number = request.form.get('number')
        try:
            number.isdigit()
            if '.' in number:
                number = float(request.form.get('number'))
            else:
                number = int(request.form.get('number'))
            square_number = str(number ** 2)
        except ValueError:
            flash('Необходимо ввести число!', 'danger')
            return redirect(url_for('fill_form'))
        return redirect(url_for('result', number=number, square_number=square_number))
    return render_template('form_number.html', title='Задача 7')


@app.route('/redirect/<number>/<square_number>')
def result(number, square_number):
    return render_template('square_number.html', number=number, square_number=square_number, title='Квадрат числа')


if __name__ == '__main__':
    app.run(debug=True)
