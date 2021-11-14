a = {'A', 'B', 'C', 'D'}
l = [[]]
for i in a:
    l += [sub + [i] for sub in l]
print(l)