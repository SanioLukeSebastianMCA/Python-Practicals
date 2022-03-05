import csv

with open('samplecsv.csv') as file:
    data = csv.reader(file, delimiter='\t')
    for row in data:
        print(row)
