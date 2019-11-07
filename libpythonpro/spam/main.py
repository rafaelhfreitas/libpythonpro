class SenderSpam:
    def __init__(self, session, sender):
        self.session = session
        self.sender = sender

    def send_emails(self, sender, subject, body):
        for user in self.session.list():
            self.sender.send(
                sender,
                user.email,
                subject,
                body
            )
