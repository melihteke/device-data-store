from pymongo import MongoClient
from bson.objectid import ObjectId
import environment


DBA_URI = environment.DBA_URI

class DeviceDataStore:
    def __init__(self, uri, db_name, collection_name):
        self.client = MongoClient(uri)
        self.db = self.client.get_database(db_name)
        self.collection = self.db.get_collection(collection_name)

    def add_record(self, record):
        self.collection.insert_one(record)

    def remove_record(self, record_id):
        self.collection.delete_one({'_id': ObjectId(record_id)})

    def update_record(self, record_id, updates):
        self.collection.update_one({'_id': ObjectId(record_id)}, {'$set': updates})

    def view_all_records(self):
        return [record for record in self.collection.find()]

    def view_specific_record(self, filters):
        return [record for record in self.collection.find(filters)]

device_data_store = DeviceDataStore(
    uri=DBA_URI,
    db_name="infra",
    collection_name="devices"
)

while True:
    print("Options:")
    print("1. View all records")
    print("2. View specific record")
    print("3. Add record")
    print("4. Delete record")
    print("5. Update record")
    print("Q. Quit")
    choice = input("Enter an option: ").upper()

    if choice == "1":
        records = device_data_store.view_all_records()
        for record in records:
            print(record)

    elif choice == "2":
        name = input("Enter name of record to view: ")
        filters = {"name": name}
        records = device_data_store.view_specific_record(filters)
        for record in records:
            print(record)

    elif choice == "3":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        record = {"name": name, "phone": phone}
        device_data_store.add_record(record)
        print("Record added successfully!")

    elif choice == "4":
        record_id = input("Enter ID of record to delete: ")
        device_data_store.remove_record(record_id)
        print("Record deleted successfully!")

    elif choice == "5":
        record_id = input("Enter ID of record to update: ")
        name = input("Enter new name (leave blank to keep current name): ")
        device_data_store = input("Enter new phone number (leave blank to keep current phone number): ")
        updates = {}
        if name:
            updates["name"] = name
        if phone:
            updates["phone"] = phone
        device_data_store.update_record(record_id, updates)
        print("Record updated successfully!")

    elif choice == "Q":
        print("Exiting program...")
        break

    else:
        print("Invalid option. Please try again.")


