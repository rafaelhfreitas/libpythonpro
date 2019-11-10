from unittest.mock import Mock

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
    sender = Mock()
    sender_spam = SenderSpam(session, sender)
    sender_spam.send_emails(
        'oraffaudi@gmail.com',
        'Curso Python Pro',
        'Confira os novos modulos'
    )
    assert len(users) == sender.send.call_count


class SenderMock(Sender):

    def __init__(self):
        super().__init__()
        self.sent_params = None
        self.qty_sent_emails = 0

    def send(self, sender, recipient, subject, body):
        self.sent_params = (sender, recipient, subject, body)
        self.qty_sent_emails += 1


def test_params_spam(session):
    user = User(name='Rafael', email='oraffaudi@gmail.com')
    session.save(user)
    sender = Mock()
    sender_spam = SenderSpam(session, sender)
    sender_spam.send_emails(
        'rafaelfreitas@gmail.com',
        'Curso Python Pro',
        'Confira os novos modulos'
    )

    sender.send.assert_called_once_with(
        'rafaelfreitas@gmail.com',
        'oraffaudi@gmail.com',
        'Curso Python Pro',
        'Confira os novos modulos'
    )
