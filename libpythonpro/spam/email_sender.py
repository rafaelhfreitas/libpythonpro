class Sender():
    def __init__(self):
        self.qty_sent_emails = 0

    def send(self, sender, recipient, subject, body):
        if '@' not in sender:
            raise InvalidEmail(f'Email de remetente inválido: {sender}')
        self.qty_sent_emails += 1
        return sender


class InvalidEmail(Exception):
    pass
