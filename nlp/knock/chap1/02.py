s1 = 'パトカー'
s2 = 'タクシー'

l = [s1[i] + s2[i] for i in range(len(s1))]

print(''.join(l))