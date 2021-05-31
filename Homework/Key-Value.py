d = {'name': 'ivan', 'surname': 'ivanov'}
d1 = {v: k for k, v in d.items()}
print(f'{d} -> {d1}')