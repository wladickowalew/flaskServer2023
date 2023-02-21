from flask import Flask, render_template
from werkzeug.utils import redirect

from data.users import User
from loginform import LoginForm
from data import db_session

app = Flask(__name__)
db_session.global_init("db/blogs.db")
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница',
                           username=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success')
def odd_even():
    return "УРАААААААА!!!!!!"

def test():
    db_sess = db_session.create_session()
    for i in range(2, 101):
        user = User()
        user.name = f"Пользователь {i}"
        user.about = f"биография пользователя {i}"
        user.email = f"email{i}@email.ru"
        db_sess.add(user)
    db_sess.commit()

if __name__ == '__main__':
    test()
    app.run(port=8080, host='127.0.0.1')