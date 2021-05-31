l = [1, 1, 2, 3, 5, 4, 5, 5, 6]

l1 = []

for i in l:
    if i not in l1:
        l1.append(i)

print(f'{l} -> {l1}')
