import pytest

from libpythonpro.spam.email_sender import Sender, InvalidEmail


def test_create_email_sender():
    sender = Sender()
    assert sender is not None


@pytest.mark.parametrize(
    'recipient',
    ['oraffaudi@gmail.com', 'o_raffa_udi@hotmail.com']
)
def test_sender(recipient):
    sender = Sender()
    result = sender.send(
        recipient,
        'rafael.freitas@bigworks.com',
        'Cursos Python Pro',
        'Turma aberta com sucesso. '
    )
    assert recipient in result


@pytest.mark.parametrize(
    'recipient',
    ['', 'o_raffa_udi']
)
def test_sender_invalid(recipient):
    sender = Sender()
    with pytest.raises(InvalidEmail):
        sender.send(
            recipient,
            'rafael.freitas@bigworks.com',
            'Cursos Python Pro',
            'Turma aberta com sucesso. '
        )
