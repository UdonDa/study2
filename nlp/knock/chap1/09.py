import random

S = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'

S_split = S.split(' ')


out = []

for s in S_split:
    if len(s) > 4:
        f = s[0]
        b = s[-1]
        m = list(s[1:-1])
        random.shuffle(m)
        m = ''.join(m)
        s = f + m + b
    out.append(s)
    
print(' '.join(out))