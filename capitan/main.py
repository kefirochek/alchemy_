from class_work.data import db_session
from flask import Flask
from class_work.data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    # app.run()
    user = User()
    user.name = "Пользователь 6"
    user.about = "биография пользователя 6"
    user.email = "666@email.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.name = "Пользователь 7"
    user.about = "биография пользователя 7"
    user.email = "777@email.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.name = "Пользователь 9"
    user.about = "биография пользователя 9"
    user.email = "fhjjf@email.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()