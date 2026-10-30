from uuid import uuid1

class Lead:
    def __init__(self, name, email, contact, status) -> None:
        self.id = uuid1().int
        self.name = name 
        self.email = email
        self.contact = contact
        self.status = status




