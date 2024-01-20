
import json
from pprint import pprint

import connect
from models import Quote, Author

def find_name(name):
    i = Author.objects.get(fullname = name).id
    return i


def find_tag(txt):
    i = Quote.objects.get(tags = txt).id
    return i


def find_tags(name):
    i = Author.objects.get(fullname = name).id
    return i


