## Creating a device datastore with MongoDB

Welcome to the device data store application readme! This application is designed to showcase how easy it is to build a device data storage using MongoDB and Python. Although this is very basicimplementation of No-SQL DB, the purpose of this application is to demonstrate how NoSQL databases like MongoDB can be used in different fields, such as network automation as well.

As a network engineer, you may need to store various types of data such as device names, site information, IP addresses, device statuses, contact information, and subnets and etc.. Instead of using traditional relational databases or anoy other storing types, NoSQL databases like MongoDB can provide greater flexibility and scalability in managing and organizing this data.

To get started with the data store application, please ensure that you have access to a MongoDB instance. In this example, I have used the FreeTier option available on https://cloud.mongodb.com/. However, you can use any MongoDB instance that is accessible to you.

Here are the steps to set up and run the application:

Clone the repository to your local machine.
Install the required dependencies by running pip install -r requirements.txt.
Set up a .env file with the necessary environment variables for connecting to your MongoDB instance (e.g. DBA_URI).
Start the application by running python app.py.
By following these steps, you can quickly set up and use the phonebook application to explore the features and benefits of using MongoDB as your NoSQL database.


## How to Run the app

```sh
git clone https://github.com/melihteke/phonebook.git

python3 -m venv .venv

pip install --upgrade pip

pip install -r requirements.txt

source .venv/bin/activate


(.venv) MTeke1@APKM2W42362BA4 device-data-store % python app.py 
Options:
1. View all records
2. View specific record
3. Add record
4. Delete record
5. Update record
Q. Quit
Enter an option: 1
{'_id': ObjectId('6436ee1644336b29c882e323'), 'hostname': 'DEV2011R01', 'device_type': 'router', 'site_number': '2011', 'site': 'Slough', 'status': 'Operational', 'local_subnets': ['10.11.1.0/24', '10.11.2.0/24', '10.11.3.0/24'], 'wan_a_provider': 'GTT', 'wan_a_ip_setting': 'dhcp', 'wan_b_provider': 'BT', 'wan_b_ip_setting': '203.45.23.143/30', 'hardware': 'C1111-4PLTEEA', 'serial': 'FOC2XXX7L5K9', 'vlans': ['8', '110'], 'l3_ints': ['GigabitEthernet0/0/0', 'GigabitEthernet0/0/1'], 'l2_ints': ['GigabitEthernet0/1/0', 'GigabitEthernet0/1/1', 'GigabitEthernet0/1/2', 'GigabitEthernet0/1/3']}
{'_id': ObjectId('6436eec044336b29c882e324'), 'hostname': 'DEV2012R01', 'device_type': 'router', 'site_number': '2012', 'site': 'Dublin', 'status': 'Operational', 'local_subnets': ['10.12.1.0/24', '10.12.2.0/24', '10.12.3.0/24'], 'wan_a_provider': 'GTT', 'wan_a_ip_setting': 'dhcp', 'wan_b_provider': 'BT', 'wan_b_ip_setting': '213.45.23.143/30', 'hardware': 'C1111-4PLTEEA', 'serial': 'FOC2XXX7L599', 'vlans': ['8', '110'], 'l3_ints': ['GigabitEthernet0/0/0', 'GigabitEthernet0/0/1'], 'l2_ints': ['GigabitEthernet0/1/0', 'GigabitEthernet0/1/1', 'GigabitEthernet0/1/2', 'GigabitEthernet0/1/3']}
{'_id': ObjectId('6436eedb44336b29c882e325'), 'hostname': 'DEV2013R01', 'device_type': 'router', 'site_number': '2013', 'site': 'Norwich', 'status': 'Operational', 'local_subnets': ['10.13.1.0/24', '10.13.2.0/24', '10.13.3.0/24'], 'wan_a_provider': 'Verizon', 'wan_a_ip_setting': 'dhcp', 'wan_b_provider': 'BT', 'wan_b_ip_setting': '46.45.23.143/30', 'hardware': 'C1111-4PLTEEA', 'serial': 'FOC2XXX7DH9', 'vlans': ['8', '110'], 'l3_ints': ['GigabitEthernet0/0/0', 'GigabitEthernet0/0/1'], 'l2_ints': ['GigabitEthernet0/1/0', 'GigabitEthernet0/1/1', 'GigabitEthernet0/1/2', 'GigabitEthernet0/1/3']}
{'_id': ObjectId('6436f09444336b29c882e326'), 'hostname': 'DEV2010R01', 'device_type': 'router', 'site_number': '2010', 'site': 'Croydon', 'status': 'Operational', 'local_subnets': ['10.10.1.0/24', '10.10.2.0/24', '10.10.3.0/24'], 'wan_a_provider': 'BT', 'wan_a_ip_setting': 'dhcp', 'wan_b_provider': 'BT', 'wan_b_ip_setting': '32.45.31.141/30', 'hardware': 'C1111-4PLTEEA', 'serial': 'FOCXXSDF5K9', 'vlans': ['8', '110'], 'l3_ints': ['GigabitEthernet0/0/0', 'GigabitEthernet0/0/1'], 'l2_ints': ['GigabitEthernet0/1/0', 'GigabitEthernet0/1/1', 'GigabitEthernet0/1/2', 'GigabitEthernet0/1/3']}



Options:
1. View all records
2. View specific record
3. Add record
4. Delete record
5. Update record
Q. Quit
Enter an option: 2
Enter hostname of record to view: DEV2013R01
{'_id': ObjectId('6436eedb44336b29c882e325'), 'hostname': 'DEV2013R01', 'device_type': 'router', 'site_number': '2013', 'site': 'Norwich', 'status': 'Operational', 'local_subnets': ['10.13.1.0/24', '10.13.2.0/24', '10.13.3.0/24'], 'wan_a_provider': 'Verizon', 'wan_a_ip_setting': 'dhcp', 'wan_b_provider': 'BT', 'wan_b_ip_setting': '46.45.23.143/30', 'hardware': 'C1111-4PLTEEA', 'serial': 'FOC2XXX7DH9', 'vlans': ['8', '110'], 'l3_ints': ['GigabitEthernet0/0/0', 'GigabitEthernet0/0/1'], 'l2_ints': ['GigabitEthernet0/1/0', 'GigabitEthernet0/1/1', 'GigabitEthernet0/1/2', 'GigabitEthernet0/1/3']}



Options:
1. View all records
2. View specific record
3. Add record
4. Delete record
5. Update record
Q. Quit
Enter an option: 3
Enter hostname of the record:DEVMELIH
Enter device_type of the record:router
Enter site_number of the record:41383
Enter site of the record:Amsterdam
Enter status of the record:Operational
Enter local_subnets of the record:['10.10.14.0/24', '10.10.15.0/25']
Enter wan_a_provider of the record:GTT
Enter wan_a_ip_setting of the record:dhcp
Enter wan_b_provider of the record:BT
Enter wan_b_ip_setting of the record:dhcp
Enter hardware of the record:C1111
Enter serial of the record:FGPZ23432XC
Enter vlans of the record:['56', '8']
Enter l3_ints of the record:['Gi0/0/0', 'Gi0/0/1']
Enter l2_ints of the record:Gi0/1/0
Record added successfully!
Options:
1. View all records
2. View specific record
3. Add record
4. Delete record
5. Update record
Q. Quit
Enter an option: 1
{'_id': ObjectId('6436ee1644336b29c882e323'), 'hostname': 'DEV2011R01', 'device_type': 'router', 'site_number': '2011', 'site': 'Slough', 'status': 'Operational', 'local_subnets': ['10.11.1.0/24', '10.11.2.0/24', '10.11.3.0/24'], 'wan_a_provider': 'GTT', 'wan_a_ip_setting': 'dhcp', 'wan_b_provider': 'BT', 'wan_b_ip_setting': '203.45.23.143/30', 'hardware': 'C1111-4PLTEEA', 'serial': 'FOC2XXX7L5K9', 'vlans': ['8', '110'], 'l3_ints': ['GigabitEthernet0/0/0', 'GigabitEthernet0/0/1'], 'l2_ints': ['GigabitEthernet0/1/0', 'GigabitEthernet0/1/1', 'GigabitEthernet0/1/2', 'GigabitEthernet0/1/3']}
{'_id': ObjectId('6436eec044336b29c882e324'), 'hostname': 'DEV2012R01', 'device_type': 'router', 'site_number': '2012', 'site': 'Dublin', 'status': 'Operational', 'local_subnets': ['10.12.1.0/24', '10.12.2.0/24', '10.12.3.0/24'], 'wan_a_provider': 'GTT', 'wan_a_ip_setting': 'dhcp', 'wan_b_provider': 'BT', 'wan_b_ip_setting': '213.45.23.143/30', 'hardware': 'C1111-4PLTEEA', 'serial': 'FOC2XXX7L599', 'vlans': ['8', '110'], 'l3_ints': ['GigabitEthernet0/0/0', 'GigabitEthernet0/0/1'], 'l2_ints': ['GigabitEthernet0/1/0', 'GigabitEthernet0/1/1', 'GigabitEthernet0/1/2', 'GigabitEthernet0/1/3']}
{'_id': ObjectId('6436eedb44336b29c882e325'), 'hostname': 'DEV2013R01', 'device_type': 'router', 'site_number': '2013', 'site': 'Norwich', 'status': 'Operational', 'local_subnets': ['10.13.1.0/24', '10.13.2.0/24', '10.13.3.0/24'], 'wan_a_provider': 'Verizon', 'wan_a_ip_setting': 'dhcp', 'wan_b_provider': 'BT', 'wan_b_ip_setting': '46.45.23.143/30', 'hardware': 'C1111-4PLTEEA', 'serial': 'FOC2XXX7DH9', 'vlans': ['8', '110'], 'l3_ints': ['GigabitEthernet0/0/0', 'GigabitEthernet0/0/1'], 'l2_ints': ['GigabitEthernet0/1/0', 'GigabitEthernet0/1/1', 'GigabitEthernet0/1/2', 'GigabitEthernet0/1/3']}
{'_id': ObjectId('6436f09444336b29c882e326'), 'hostname': 'DEV2010R01', 'device_type': 'router', 'site_number': '2010', 'site': 'Croydon', 'status': 'Operational', 'local_subnets': ['10.10.1.0/24', '10.10.2.0/24', '10.10.3.0/24'], 'wan_a_provider': 'BT', 'wan_a_ip_setting': 'dhcp', 'wan_b_provider': 'BT', 'wan_b_ip_setting': '32.45.31.141/30', 'hardware': 'C1111-4PLTEEA', 'serial': 'FOCXXSDF5K9', 'vlans': ['8', '110'], 'l3_ints': ['GigabitEthernet0/0/0', 'GigabitEthernet0/0/1'], 'l2_ints': ['GigabitEthernet0/1/0', 'GigabitEthernet0/1/1', 'GigabitEthernet0/1/2', 'GigabitEthernet0/1/3']}
{'_id': ObjectId('6436fc798b66115eda7fccc7'), 'hostname': 'DEVMELIH', 'device_type': 'router', 'site_number': '41383', 'site': 'Amsterdam', 'status': 'Operational', 'local_subnets': "['10.10.14.0/24', '10.10.15.0/25']", 'wan_a_provider': 'GTT', 'wan_a_ip_setting': 'dhcp', 'wan_b_provider': 'BT', 'wan_b_ip_setting': 'dhcp', 'hardware': 'C1111', 'serial': 'FGPZ23432XC', 'vlans': "['56', '8']", 'l3_ints': "['Gi0/0/0', 'Gi0/0/1']", 'l2_ints': 'Gi0/1/0'}



DELETING AN ENTRY
Options:
1. View all records
2. View specific record
3. Add record
4. Delete record
5. Update record
Q. Quit
Enter an option: 4
Enter ID of record to delete: 6436fc798b66115eda7fccc7
Record deleted successfully!
Options:
1. View all records
2. View specific record
3. Add record
4. Delete record
5. Update record
Q. Quit
Enter an option: 1

THERE IS NO ENTRY 4 ANYMORE
{'_id': ObjectId('6436ee1644336b29c882e323'), 'hostname': 'DEV2011R01', 'device_type': 'router', 'site_number': '2011', 'site': 'Slough', 'status': 'Operational', 'local_subnets': ['10.11.1.0/24', '10.11.2.0/24', '10.11.3.0/24'], 'wan_a_provider': 'GTT', 'wan_a_ip_setting': 'dhcp', 'wan_b_provider': 'BT', 'wan_b_ip_setting': '203.45.23.143/30', 'hardware': 'C1111-4PLTEEA', 'serial': 'FOC2XXX7L5K9', 'vlans': ['8', '110'], 'l3_ints': ['GigabitEthernet0/0/0', 'GigabitEthernet0/0/1'], 'l2_ints': ['GigabitEthernet0/1/0', 'GigabitEthernet0/1/1', 'GigabitEthernet0/1/2', 'GigabitEthernet0/1/3']}
{'_id': ObjectId('6436eec044336b29c882e324'), 'hostname': 'DEV2012R01', 'device_type': 'router', 'site_number': '2012', 'site': 'Dublin', 'status': 'Operational', 'local_subnets': ['10.12.1.0/24', '10.12.2.0/24', '10.12.3.0/24'], 'wan_a_provider': 'GTT', 'wan_a_ip_setting': 'dhcp', 'wan_b_provider': 'BT', 'wan_b_ip_setting': '213.45.23.143/30', 'hardware': 'C1111-4PLTEEA', 'serial': 'FOC2XXX7L599', 'vlans': ['8', '110'], 'l3_ints': ['GigabitEthernet0/0/0', 'GigabitEthernet0/0/1'], 'l2_ints': ['GigabitEthernet0/1/0', 'GigabitEthernet0/1/1', 'GigabitEthernet0/1/2', 'GigabitEthernet0/1/3']}
{'_id': ObjectId('6436eedb44336b29c882e325'), 'hostname': 'DEV2013R01', 'device_type': 'router', 'site_number': '2013', 'site': 'Norwich', 'status': 'Operational', 'local_subnets': ['10.13.1.0/24', '10.13.2.0/24', '10.13.3.0/24'], 'wan_a_provider': 'Verizon', 'wan_a_ip_setting': 'dhcp', 'wan_b_provider': 'BT', 'wan_b_ip_setting': '46.45.23.143/30', 'hardware': 'C1111-4PLTEEA', 'serial': 'FOC2XXX7DH9', 'vlans': ['8', '110'], 'l3_ints': ['GigabitEthernet0/0/0', 'GigabitEthernet0/0/1'], 'l2_ints': ['GigabitEthernet0/1/0', 'GigabitEthernet0/1/1', 'GigabitEthernet0/1/2', 'GigabitEthernet0/1/3']}
{'_id': ObjectId('6436f09444336b29c882e326'), 'hostname': 'DEV2010R01', 'device_type': 'router', 'site_number': '2010', 'site': 'Croydon', 'status': 'Operational', 'local_subnets': ['10.10.1.0/24', '10.10.2.0/24', '10.10.3.0/24'], 'wan_a_provider': 'BT', 'wan_a_ip_setting': 'dhcp', 'wan_b_provider': 'BT', 'wan_b_ip_setting': '32.45.31.141/30', 'hardware': 'C1111-4PLTEEA', 'serial': 'FOCXXSDF5K9', 'vlans': ['8', '110'], 'l3_ints': ['GigabitEthernet0/0/0', 'GigabitEthernet0/0/1'], 'l2_ints': ['GigabitEthernet0/1/0', 'GigabitEthernet0/1/1', 'GigabitEthernet0/1/2', 'GigabitEthernet0/1/3']}



```

![image](https://user-images.githubusercontent.com/36086368/231555655-378f5b49-016f-45b8-8ae5-4e14817c3f84.png)


![image](https://user-images.githubusercontent.com/36086368/231555588-db7a3ae5-9aa6-4877-ba36-173de9e9f98e.png)


![image](https://user-images.githubusercontent.com/36086368/231555723-8cfc5071-d65d-4315-9eff-bf1d3daa3690.png)

