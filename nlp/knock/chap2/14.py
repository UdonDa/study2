import sys

N = int(sys.argv[1])

path = './popular-names.txt'

with open(path, 'r') as f:
    f = f.readlines()
    # print(f)
    of = f[:N]
    of = ''.join(of)
    
    print(of)
