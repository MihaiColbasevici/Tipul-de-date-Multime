a = {1, 2, 3, 4}
l = [[]]
for i in a:
    l += [sub + [i] for sub in l]
print(l)