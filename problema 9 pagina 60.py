a = set(str(input('Dati multimea A: ')))
b = set(str(input('Dati multimea B: ')))
if (all(x.isupper() for x in a)) and (all(x.isupper() for x in b)) == True:
    print('Intersectia multimilor A si B -> ', a.intersection(b))
    print('Reuniunea multimilor A si B -> ', a.union(b))
    print('Diferenta multimilor A si B -> ', a.difference(b))
    print('Diferenta multimilor B si A -> ', b.difference(a))
else:
    print('Toate elementele trebuie sa fie litere mari!')
