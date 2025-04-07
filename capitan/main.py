from datetime import datetime

from capitan.data.jobs import Jobs
from class_work.data import db_session
from flask import Flask
from class_work.data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    # app.run()
    # user = User()
    # user.name = "Пользователь 1"
    # user.about = "биография пользователя 1"
    # user.email = "email@email.ru"
    # db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.commit()

    jobs = Jobs()
    jobs.team_leader = 1
    jobs.job = 'deployment of residential modules 1 and 2'
    jobs.work_size = 15
    jobs.collaborators = '2, 3'
    jobs.start_date = datetime.now()
    jobs.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(jobs)
    db_sess.commit()


if __name__ == '__main__':
    main()