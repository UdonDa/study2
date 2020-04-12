import sys

N = int(sys.argv[1])

path = './popular-names.txt'

with open(path, 'r') as f:
    f = f.readlines()
    
    o = []
    thres = len(f) // N
    for i in range(N):
        o.append(f[i:i+thres])
    
    # if (i + thres) < len(f):
    #     o[-1] = o[-1] + f[i+thres:]
    
    
    print(o)
    print(len(o), len(o[0]))
    
    print(sum([len(l) for l in o]))
