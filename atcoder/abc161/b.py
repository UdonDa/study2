def main():
    N, M = map(int, input().split(' '))
    An = list(map(int, input().split(' ')))
    thres = sum(An) / (4 * M)
    
    count = 0
    for a in An:
        if not thres > a:
            count += 1
            
    if count >= M:
        print('Yes')
    else:
        print('No')
    
    
    
    
main()