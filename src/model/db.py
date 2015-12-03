from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

Engine = None
Session = None
Base = declarative_base()


def connect(*args, **kwargs):
    """
    It connects to the database and create a working session

    :param args: args for engine
    :param kwargs: kargs for engine
    :return: nothing
    """

    global Engine, Session, Base
    Engine = create_engine(*args, **kwargs)
    # thread-safe session
    Session = scoped_session(sessionmaker(autocommit=False,
                                          autoflush=False,
                                          bind=Engine))
    Base.query = Session.query_property()


def rebuild():
    import db_model
    Base.metadata.create_all(bind=Engine)


def get_session():
    """
    :rtype: sqlalchemy.orm.session.Session
    """
    return Session()


def initialize(app):
    connect(app.config.get('DATABASE_URI'))
    rebuild()
