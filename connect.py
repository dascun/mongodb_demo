from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://nayanpatra:RHr1G96stPY9D0eY@democluster.svpjoew.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Access a specific database (replace "your_database_name" with your actual database name)
db = client["demo_db"]

# Access a specific collection within the database (replace "your_collection_name" with your collection name)
collection = db["demo_collection"]

# Create a document (JSON-like data)
new_document = {"name": "Nayan Patra", "age": 37, "email": "dascun@example.com"}

# Insert the document into the collection
inserted_document = collection.insert_one(new_document)

# Print the inserted document's ID
print("Inserted Document ID:", inserted_document.inserted_id)

# Find a document in the collection
query = {"name": "Nayan Patra"}
result = collection.find_one(query)

if result:
    print("Found Document:", result)
else:
    print("Document not found.")
