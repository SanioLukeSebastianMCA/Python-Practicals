import csv
with open("samplecsv1.csv", newline='') as csvfile:
    d = csv.DictReader(csvfile)
    print("Name Price Quantity")
    print("--------------------")
    for i in d:
        print(i['Name'], i['Price'], i['Quantity'])
