class Sender():
    def send(self, sender, recipient, subject, body):
        if '@' not in sender:
            raise InvalidEmail(f'Email de remetente inválido: {sender}')
        return sender


class InvalidEmail(Exception):
    pass