import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class User(SqlAlchemyBase):
    def __init__(self):
        __tablename__ = 'users'

        surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
        name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
        age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
        position = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
        speciality = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
        address = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
        email = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=True)
        hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
        modified_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
        jobs = orm.relationship("Jobs", back_populates='user')
        self.id = id
        self.name = name
        self.surname = surname
        self.adress = address

    def __repr__(self):
        return f'<Colonist> {self.id} {self.name} {self.surname}'