
import connect

import re
from pprint import pprint
from models import Quote, Author, Contact
from crud import *

def func_name(txt:str):
    txt = txt.strip()
    author_id = Author.objects.get(fullname__istartswith = txt)
    res = []
    lst = Quote.objects(author = author_id)
    for i in lst:
        res.extend(i.tags)
    print(res)


def func_tag(txt):
    res = []
    txt = txt.strip()
    txt = f"{txt}.*"
    print(txt)
    regex = re.compile(txt)
    cont = Quote.objects(tags__iregex = regex  )
    for i in cont:
        res.append(i.quote.encode('utf-8'))
    print(res)


def func_tags(txt):
    res = []
    txt = txt.strip()
    lst = txt.split(",")
    quotes = Quote.objects(tags__in = lst )
    for i in quotes:
        res.append(i.quote.encode('utf-8'))
    print(res)


if __name__ == '__main__':
    pprint ("starting...")

    while True:
        text = input(">>>")
        command = text.split(":")
        if command[0] == "exit":
            break
        if len(command) > 1:
            match command[0].strip():
                case "name":
                    func_name(command[1])
                case "tags":
                    func_tags(command[1])
                case "tag":
                    func_tag(command[1])
                case _:
                    print("no valid command")
        else:
            pprint("error arguments")
        