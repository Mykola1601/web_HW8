
import json
from pprint import pprint

import connect
from models import Quote, Author


def autors_add(authors):
    for i in authors:
        i = Author(**i).save()
        pprint(i)

def quotes_add(qoutes):
    for i in qoutes:
        i["author"] = Author.objects.get(fullname = i["author"]).id
        m = Quote(**i).save()
        pprint(m)



if __name__ == '__main__':
    with open("authors.json") as file:
        authors = json.load(file)
    autors_add(authors=authors)

    with open("qoutes.json") as file:
        qoutes = json.load(file)
    quotes_add(qoutes)