
from models import Quote, Author
import connect
from pprint import pprint
import json

def find_name(name):
    i = Author.objects.get(fullname = name).id
    return i

def find_tag(txt):
    i = Quote.objects.get(tags = txt).id
    return i

def find_tags(name):
    i = Author.objects.get(fullname = name).id
    return i

pprint(find_name("Albert Einstein"))




