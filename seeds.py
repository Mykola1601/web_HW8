from models import Quote, Author
from pprint import pprint
import connect
import json


with open("authors.json") as file:
    authors = json.load(file)
for i in authors:
    i = Author(**i).save()
    pprint(i)


with open("qoutes.json") as file:
    qoutes = json.load(file)
for i in qoutes:
    i["author"] = Author.objects.get(fullname = i["author"]).id
    m = Quote(**i).save()
    pprint(m)



