
from models import Quote, Author
import connect
from pprint import pprint
import json

def find_name(name):
    i = Author.objects.get(fullname = name).id
    return i

# pprint(find_one())




