
def main():
    N, K = map(int, input().split(' '))
    
    # out = min(float('inf'), N)
    prev = N % K
    
    isFinish = False
    
    if prev == 0:
        print(0)
        return
    
    while not isFinish:
        next = abs(prev - K)
        
        if next >= prev:
            isFinish = True
        else:
            prev = next
            
    print(prev)

main()