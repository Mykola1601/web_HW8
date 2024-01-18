
# import connect
from pprint import pprint
from crud import *

def func_name(txt:str):
    txt = txt.strip()
    pprint(txt)


def func_tag(txt):
    txt = txt.strip()
    lst = Quote.objects(tags = txt)
    for i in lst:
        i= i.to_mongo().to_dict()
        print(i["quote"], "\n")


def func_tags(txt):
    tags = txt.split(",")
    # lst = Quote.objects(tags == tags[1] or tags == tags[0])
    # for i in lst:
    #     i= i.to_mongo().to_dict()
    #     print(i["quote"], "\n")



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
        