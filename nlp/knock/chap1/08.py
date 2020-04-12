def cipher(S):
    out = []
    for s in S:
        if s.islower():
            out.append(chr(219 - ord(s)))
        else:
            out.append(s)
    return ''.join(out)

S = 'I like Kubota miyu so Much'
# S = ''.join(S.split(' '))
print('In:', S)

out = cipher(S)

print('Out:', out)