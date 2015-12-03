from sqlalchemy import (
    Column,
    Integer,
    String
)
from sqlalchemy.orm import (
    relationship,
    synonym
)
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import Base


class Users(Base):
    """
    This class represents the table ``api_users`` on ORM.
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(15), unique=True, nullable=False)
    _password = Column('password', String(256), nullable=False)
    email = Column(String(25), unique=True, nullable=False)
    picture = Column(String(25), unique=True, nullable=False)

    def __init__(self, username="", password="", email="", picture=""):
        super(Users, self).__init__()
        self.username = username
        self.password = password
        self.email = email
        self.picture = picture

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, passwd):
        self._password = passwd

    password = synonym('_password', descriptor=password)

    def __repr__(self):
        return self.username


class Ranges(Base):
    """
    This class represents the table ``ranges`` on ORM.
    """

    __tablename__ = 'ranges'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    cidr = Column(String(19), nullable=False)
    # domain_ids = Column(Integer, ForeignKey('domains.id'), nullable=False)

    def __init__(self, range_name="", range_cidr="", domain_id=""):
        super(Ranges, self).__init__()
        self.name = range_name
        self.cidr = range_cidr
        self.domain_ids = domain_id

    def __repr__(self):
        return self.name
