import pytest

from libpythonpro.spam.email_sender import Sender
from libpythonpro.spam.main import SenderSpam
from libpythonpro.spam.models import User


@pytest.mark.parametrize(
    'users',
    [
        [
            User(name='Rafael', email='oraffaudi@gmail.com'),
            User(name='Henrique', email='oraffaudi@gmail.com')
        ],
        [
            User(name='Rafael', email='oraffaudi@gmail.com')
        ]
    ]
)
def test_send_spam(session, users):
    for user in users:
        session.save(user)
    sender = Sender()
    sender_spam = SenderSpam(session, sender)
    sender_spam.send_emails(
        'oraffaudi@gmail.com',
        'Curso Python Pro',
        'Confira os novos modulos'
    )
    assert len(users) == sender.qty_sent_emails
