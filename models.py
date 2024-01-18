
from mongoengine import EmbeddedDocument, Document, CASCADE
from mongoengine.fields import BooleanField, DateTimeField,  ListField, StringField, ReferenceField


class Author(Document):
    fullname = StringField()
    born_date = DateTimeField(default="11.11.1111")
    born_location = StringField()
    description = StringField()
    

class Quote(Document):
    tags = ListField()
    author = ReferenceField(Author, required=True, reverse_delete_rule=CASCADE)
    quote = StringField()
    



