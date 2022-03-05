import csv

field_name = ['Sr. No', 'Brand', 'Device Name']
Devices = [
    {'Sr. No': 1, 'Brand': 'Samsung', 'Device Name': 'Samsung A20'},
    {'Sr. No': 2, 'Brand': '1 Plus', 'Device Name': '1 Plus 9R'},
    {'Sr. No': 3, 'Brand': 'Blackberry', 'Device Name': 'Blackberry B45'},
    {'Sr. No': 4, 'Brand': 'MI', 'Device Name': 'Redmi 6A'},
    {'Sr. No': 5, 'Brand': 'POCO', 'Device Name': 'POCO M3 Pro'}]

with open('devices.csv', 'w') as csvfile:
    write = csv.DictWriter(csvfile, fieldnames=field_name)
    write.writeheader()
    write.writerows(Devices)
with open('Devices.csv', newline='') as csvfile:
    d = csv.reader(csvfile, delimiter='|')
    for r in d:
        print(','.join(r))
