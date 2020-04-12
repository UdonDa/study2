path = './popular-names.txt'

with open(path, 'r') as f:
    f = f.readlines()
    f = [s.replace('\t', ' ') for s in f]
    
    out_path = './11_out.txt'
    with open(out_path, 'w') as fw:
        fw.writelines(f)