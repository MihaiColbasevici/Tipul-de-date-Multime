sir1 = str(input('Primul sir -> '))
sir2 = str(input('Al doilea sir -> '))
a, b = set(), set()
for i in sir1:
    a.add(i)
for i in sir2:
    b.add(i)
print('Cel putin in unul dintre siruri se intalnesc caracterele: ', *sorted(a.union(b)))
print('Apar in ambele siruri caracterele: ', *sorted(a.intersection(b)))
print('Apar doar in primul sir caracterele: ', *sorted(a.difference(b)))