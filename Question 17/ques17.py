d1 = {"Name": "Daniel", "Age": 21}
d2 = {"designation": "Data Analyst", "salary": 30000}
print(f'Before : {d1}')
d1.update(d2)
print(f'After merging : {d1}')