def main():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())
    
    count = 0
    # if (500 * A + B * 100 + 50 * C) < X:
    #     print(count)
        
    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                # print(a, b, c)
                total = 500 * a + b * 100 + 50 * c
                if total == X:
                    count += 1
    print(count)
    
    

    
main()