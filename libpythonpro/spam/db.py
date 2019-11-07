from time import sleep


class Session:
    count = 0
    users = []

    def save(self, user):
        Session.count += 1
        user.id = Session.count
        self.users.append(user)

    def list(self):
        return self.users

    def rollback(self):
        self.users.clear()

    def close(self):
        pass


class Connection:

    def __init__(self):
        sleep(1)

    def create_session(self):
        return Session()

    def close(self):
        pass
