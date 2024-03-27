"""
Задание №7
📌 Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
📌 Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
📌 Данные о новостях должны быть переданы в шаблон через контекст.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def news():
    news = [{'title': 'Новость 1',
             'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Culpa, fugiat obcaecati? '
                     'Dignissimos earum facilis incidunt modi, molestias mollitia nam quis recusandae voluptatum',
             'data': '20.03.2024'},
            {'title': 'Новость 2',
             'text': 'Dicta id officia quibusdam vel voluptates. Ad adipisci aliquid animi architecto commodi deleniti'
                     ' dolor doloremque facilis fugiat hic illo nam odit officia placeat provident quam quisquam quo'
                     ' reiciendis repudiandae sint suscipit unde, velit voluptatem!',
             'data': '17.03.2024'},
            {'title': 'Новость 3',
             'text': 'Ab accusamus delectus et expedita id iste, laboriosam optio quam, recusandae sed veritatis'
                     ' voluptate! Accusamus blanditiis debitis et tempora. Ab architecto asperiores aut consequuntur '
                     'distinctio earum iusto nihil, non odit quidem soluta veniam',
             'data': '17.03.2024'},
            {'title': 'Новость 4',
             'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Culpa, fugiat obcaecati? '
                     'Dignissimos earum facilis incidunt modi, molestias mollitia nam quis recusandae voluptatum',
             'data': '21.03.2024'},
            {'title': 'Новость 5',
             'text': 'Dicta id officia quibusdam vel voluptates. Ad adipisci aliquid animi architecto commodi deleniti'
                     ' dolor doloremque facilis fugiat hic illo nam odit officia placeat provident quam quisquam quo'
                     ' reiciendis repudiandae sint suscipit unde, velit voluptatem!',
             'data': '19.03.2024'},
            {'title': 'Новость 6',
             'text': 'Ab accusamus delectus et expedita id iste, laboriosam optio quam, recusandae sed veritatis'
                     ' voluptate! Accusamus blanditiis debitis et tempora. Ab architecto asperiores aut consequuntur '
                     'distinctio earum iusto nihil, non odit quidem soluta veniam',
             'data': '7.03.2024'}]
    context = {'data': news,
               'title': 'Задание №7'}
    return render_template('news.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
