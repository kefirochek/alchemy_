from class_work.data import db_session
from flask import Flask
from class_work.data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    # app.run()
    user = User()
    user.name = "Пользователь 1"
    user.about = "биография пользователя 1"
    user.email = "email111@email.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.name = "Пользователь 2"
    user.about = "биография пользователя 2"
    user.email = "email222@email.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.name = "Пользователь 3"
    user.about = "биография пользователя 3"
    user.email = "email333@email.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()