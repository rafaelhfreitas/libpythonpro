from libpythonpro.spam.models import User


def test_save_user(session):
    user = User(name='Rafael', email='oraffaudi@gmail.com')
    session.save(user)
    assert isinstance(user.id, int)


def test_list_users(session):
    users = [
        User(name='Rafael', email='oraffaudi@gmail.com'),
        User(name='Henrique', email='oraffaudi@gmail.com')
    ]
    for user in users:
        session.save(user)
    assert users == session.list()
