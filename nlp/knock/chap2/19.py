import sys

path = './popular-names.txt'

with open(path, 'r') as f:
    f = f.readlines()
    f = [s.split('\t')[0] for s in f]
    # print(f)
    
    dic = {}
    for s in f:
        if dic.get(s) is None:
            dic[s] = 1
        else:
            dic[s] += 1
    
    dic = sorted(dic.items(), key = lambda x: x[1], reverse=True)
    
    print(dic)
        