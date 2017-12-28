from django_mongokit import connection
from django_mongokit.document import DjangoDocument
from mongokit import *
connection = Connection()

@connection.register
class User(Document):
    __database__ = "tutorial"
    __collection__ = "users"
    structure = {
        "_type": unicode,
        "name": unicode,
        "is_registered": bool,
    }
    default_values = {"is_registered": False}

@connection.register
class ProfessionalUser(User):
    structure = {
        "activity": unicode,
    }

    def professional_stuff(self):
        return "stuff"