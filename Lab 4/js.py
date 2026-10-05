import json

with open("sample-data.json") as file:
    data = json.load(file)

print("Interface Status")

for item in data["imdata"]:
    a = item["l1PhysIf"]["attributes"]
    print(a["dn"], a["descr"], a["speed"], a["mtu"])

    