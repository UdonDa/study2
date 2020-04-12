import sys

path = './popular-names.txt'

with open(path, 'r') as f:
    f = f.readlines()
    f = [int(s.split('\t')[2]) for s in f]
    f = sorted(f, reverse=True)
    print(f)