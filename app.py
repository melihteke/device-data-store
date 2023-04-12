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
        hostname = input("Enter hostname of record to view: ")
        filters = {"hostname": hostname}
        records = device_data_store.view_specific_record(filters)
        for record in records:
            print(record)

    elif choice == "3":
        hostname = input("Enter hostname of the record:")
        device_type = input("Enter device_type of the record:")
        site_number = input("Enter site_number of the record:")
        site = input("Enter site of the record:")
        status = input("Enter status of the record:")
        local_subnets = input("Enter local_subnets of the record:")
        wan_a_provider = input("Enter wan_a_provider of the record:")
        wan_a_ip_setting = input("Enter wan_a_ip_setting of the record:")
        wan_b_provider = input("Enter wan_b_provider of the record:")
        wan_b_ip_setting = input("Enter wan_b_ip_setting of the record:")
        hardware = input("Enter hardware of the record:")
        serial = input("Enter serial of the record:")
        vlans = input("Enter vlans of the record:")
        l3_ints = input("Enter l3_ints of the record:")
        l2_ints = input("Enter l2_ints of the record:")
        
        record = {"hostname": hostname,
                  "device_type":device_type,
                  "site_number":site_number,
                  "site":site,
                  "status":status,
                  "local_subnets":local_subnets,
                  "wan_a_provider":wan_a_provider,
                  "wan_a_ip_setting":wan_a_ip_setting,
                  "wan_b_provider":wan_b_provider,
                  "wan_b_ip_setting":wan_b_ip_setting,
                  "hardware":hardware,
                  "serial":serial,
                  "vlans":vlans,
                  "l3_ints":l3_ints,
                  "l2_ints":l2_ints
                 }
                  
        device_data_store.add_record(record)
        print("Record added successfully!")

    elif choice == "4":
        record_id = input("Enter ID of record to delete: ")
        device_data_store.remove_record(record_id)
        print("Record deleted successfully!")

    elif choice == "5":
        record_id = input("Enter ID of record to update: ")
        
        hostname = input("Enter hostname of the record(leave blank to keep current name):")
        device_type = input("Enter device_type of the record(leave blank to keep current name):")
        site_number = input("Enter site_number of the record(leave blank to keep current name):")
        site = input("Enter site of the record(leave blank to keep current name):")
        status = input("Enter status of the record(leave blank to keep current name):")
        local_subnets = input("Enter local_subnets of the record(leave blank to keep current name):")
        wan_a_provider = input("Enter wan_a_provider of the record(leave blank to keep current name):")
        wan_a_ip_setting = input("Enter wan_a_ip_setting of the record(leave blank to keep current name):")
        wan_b_provider = input("Enter wan_b_provider of the record(leave blank to keep current name):")
        wan_b_ip_setting = input("Enter wan_b_ip_setting of the record(leave blank to keep current name):")
        hardware = input("Enter hardware of the record(leave blank to keep current name):")
        serial = input("Enter serial of the record(leave blank to keep current name):")
        vlans = input("Enter vlans of the record(leave blank to keep current name):")
        l3_ints = input("Enter l3_ints of the record(leave blank to keep current name):")
        l2_ints = input("Enter l2_ints of the record(leave blank to keep current name):")

        updates = {}
        if hostname:
            updates["hostname"] = hostname
        if device_type:
            updates["device_type"] = device_type
        if site_number:
            updates["site_number"] = site_number
        if site:
            updates["site"] = site
        if status:
            updates["status"] = status
        if local_subnets:
            updates["local_subnets"] = local_subnets
        if wan_a_provider:
            updates["wan_a_provider"] = wan_a_provider
        if wan_a_ip_setting:
            updates["wan_a_ip_setting"] = wan_a_ip_setting
        if wan_b_provider:
            updates["wan_b_provider"] = wan_b_provider
        if wan_b_ip_setting:
            updates["wan_b_ip_setting"] = wan_b_ip_setting
        if hardware:
            updates["hardware"] = hardware
        if serial:
            updates["serial"] = serial
        if vlans:
            updates["vlans"] = vlans
        if l3_ints:
            updates["l3_ints"] = l3_ints
        if l2_ints:
            updates["l2_ints"] = l2_ints
            
            
        device_data_store.update_record(record_id, updates)
        print("Record updated successfully!")

    elif choice == "Q":
        print("Exiting program...")
        break

    else:
        print("Invalid option. Please try again.")


