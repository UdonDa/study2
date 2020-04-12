s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
s = ''.join(s.split(' '))
s = list(s)


dic = {}
for n in s:
    if dic.get(n) is None:
        dic[n] = 1
    else:
        dic[n] += 1

out = [n for n in dic.values()]
print(out)
