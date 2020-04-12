def main():
    N = int(input())
    An = list(map(int, input().split(' ')))
    
    isFinish = False
    count = 0
    while not isFinish:
        FALG = False
        for a in An:
            if a % 2 == 1:
                FALG = True
        if FALG:
            isFinish = True
            break
        count += 1
        An = [a // 2 for a in An]
        
    print(count)
    
main()