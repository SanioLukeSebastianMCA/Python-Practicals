print("\n\nSort dictionary in ascending and descending order.\n")
d1 = {'Besanio': 31, 'Avil': 27, 'Tejas': 21, 'Nebin': 25, 'Vikram': 23, 'Winston': 12, 'Shantanu': 13, 'Vivek': 32,
      'Benjamin': 8, 'Valle': 32}

print(f'Name list : {d1}\n')
print(f'Ascending ordered name list : {dict(sorted(d1.items()))}')
print(f'Decending ordered name list : {dict(sorted(d1.items(), reverse=True))}')