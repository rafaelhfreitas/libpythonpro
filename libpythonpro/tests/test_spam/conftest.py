import pytest

from libpythonpro.spam.db import Connection


@pytest.fixture(scope='session')
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
