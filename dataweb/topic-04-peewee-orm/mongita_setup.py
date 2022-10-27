from mongita import MongitaClientDisk
client = MongitaClientDisk()
from bson.objectid import ObjectId

shopping_db = client.shopping_db
list_collection = shopping_db.list_collection

list_collection.insert_many([
        { "description": 'apples' },
        { "description": 'broccoli' },
        { "description": 'pizza' },
        { "description": 'tangerine' },
        { "description": 'potatoes' }
    ])

items = list_collection.find()
print(items)
