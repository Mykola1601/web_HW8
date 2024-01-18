from mongoengine import connect
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

# connect to cluster on AtlasDB with connection string

connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}.x4hv9eh.mongodb.net/{db_name}?retryWrites=true&w=majority""", ssl=True)
#                        mongodb+srv://nik160186:<password>@mymongo.x4hv9eh.mongodb.net/?retryWrites=true&w=majority






