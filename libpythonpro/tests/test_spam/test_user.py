import pytest

from libpythonpro.spam.db import Connection
from libpythonpro.spam.models import User


@pytest.fixture
def connection():
    # Setup
    connection_obj = Connection()
    yield Connection()
    # TearDown
    connection_obj.close()


@pytest.fixture
def session(connection):
    session_obj = connection.create_session()
    yield session_obj
    session_obj.rollback()
    session_obj.close()


def test_save_user(session):
    user = User(name='Rafael')
    session.save(user)
    assert isinstance(user.id, int)


def test_list_users(session):
    users = [User(name='Rafael'), User(name='Henrique')]
    for user in users:
        session.save(user)
    assert users == session.list()
