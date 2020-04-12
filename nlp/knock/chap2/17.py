import sys

path = './popular-names.txt'

with open(path, 'r') as f:
    f = f.readlines()
    f = set([s.split('\t')[0] for s in f])
    
    print(f)