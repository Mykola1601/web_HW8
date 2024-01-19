
# import connect
from pprint import pprint
from crud import *

def func_name(txt:str):
    txt = txt.strip()
    author_id = Author.objects.get(fullname = txt )
    res = []
    lst = Quote.objects(author = author_id)
    for i in lst:
        res.extend(i.tags)
    print(res)


def func_tag(txt):
    func_tags(txt)

    # txt = txt.strip()
    # print(txt)
    # lst = Quote.objects(tags = txt)
    # for i in lst:
    #     i= i.to_mongo().to_dict()
    #     print(i["quote"], "\n")


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
        