from json import load, dumps

REPORT_FILE = "report.txt"
with open(REPORT_FILE, "r") as file:
        data = load(file)

# EXAMPLE ON ACESSING THE JSON DATA REPORT
print(dumps(data["INTERFACES_INFO"]["Ethernet adapter Ethernet"], indent=4))
print(dumps(data["INTERFACES_INFO"]["Ethernet adapter Ethernet"]["IPv4 Address"]))
print(dumps(data["INTERFACES_INFO"]["Ethernet adapter Ethernet"]["Physical Address"]))
