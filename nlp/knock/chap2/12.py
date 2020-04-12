path = './popular-names.txt'

with open(path, 'r') as f:
    f = f.readlines()
    f = [s.split('\t') for s in f]
    
    # print(f)
    s1 = [s[0] + '\n' for s in f]
    s2 = [s[1] + '\n' for s in f]
    
    out_s1 = './12_out_col1.txt'
    out_s2 = './12_out_col2.txt'
    for path, s in zip([out_s1, out_s2], [s1, s2]):
        with open(path, 'w') as fw:
            fw.writelines(s)