path_col1 = './12_out_col1.txt'
path_col2 = './12_out_col2.txt'
path_out = './13_out.txt'

with open(path_col1, 'r') as f1:
    with open(path_col2, 'r') as f2:
        f1 = f1.readlines()
        f2 = f2.readlines()
        
        l = [s1.replace('\n', '\t') + s2 for s1, s2 in zip(f1, f2)]
        
        with open(path_out, 'w') as f:
            f.writelines(l)