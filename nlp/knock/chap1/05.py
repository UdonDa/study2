def n_gram(S, n=1):
    out = []
    for i in range(0, len(S)-n+1):
        out.append(S[i:i+n])
    return out
    
# S = '今日はいい天気ですね。'
S = 'I am an NLPer'
print('Input:', S)

# 単語bi-gram
S_mozi = S.split(' ')
print(n_gram(S_mozi, 2))


# 文字bi-gram
S_tango = ''.join(S.split(' '))
print(n_gram(S_tango, 2))