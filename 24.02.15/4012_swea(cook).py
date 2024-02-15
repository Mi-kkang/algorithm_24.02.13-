t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    n = int(input())    # 음식 개수 받기!
    arr = [list(map(int, input().split())) for _ in range(n)]

    less_sj = 20000

    for i in range(n) :
        for j in range(n) :
            if i != j :
                a = arr[i][j] + arr[j][i]
                b = arr[n-1-i][n-1-j] + arr[n-1-j][n-1-i]

                cha = abs(a-b)

                if less_sj > cha :
                    less_sj = cha

    print(f'#{tc} {less_sj}')