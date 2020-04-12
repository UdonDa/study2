import subprocess

path = './popular-names.txt'

with open(path, 'r') as f:
    f = f.readlines()
    f = [s.replace('\t', ' ').replace('\n', '') for s in f]
    

print('行数:', len(f))

# UNIX
# cat popular-names.txt | wc -l'