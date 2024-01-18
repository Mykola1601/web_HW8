
# python - m pip install "pymongo[srv]"
from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://nik160186:16011986@mymongo.x4hv9eh.mongodb.net/?retryWrites=true&w=majority",
       server_api=ServerApi('1') )

db = client.book

# result_1 = db.authors.insert_one({"12345":"1234"})
# result_2 = db.quotes()

# print(result_1)
# print(result_2)
