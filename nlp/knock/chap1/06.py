def n_gram(S, n=1):
    out = []
    for i in range(0, len(S)-n+1):
        out.append(S[i:i+n])
    return out


s1 = 'paraparaparadise'
s2 = 'paragraph'

X = n_gram(s1, 2)
Y = n_gram(s2, 2)
print('X:', X)
print('Y:', Y)

set_X = set(X)
set_Y = set(Y)

print('和集合:', set_X.union(set_Y))
print('積集合:', set_X.intersection(set_Y))
print('差集合:', set_X.difference(set_Y))


if 'se' in set_X.union(set_Y):
    print('se in (set_X | set_Y)')