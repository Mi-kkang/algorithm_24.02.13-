def f(i, M, N, K, s, c) :       # s는 부분집합의 합, c 부분집합 원소 개수
    if N==c and K==s :
        return 1
    elif i == M :
        return 0
    elif s > K or c > N :       # 부분집합의 합이 목표보다 크거나 더 많은 원소가 선택된 경우
        return 0
    else :
        r1 = f(i+1, M, N, K, s+arr[i], c+1)  # arr[i]가 포함되는 경우
        r2 = f(i+1, M, N, K, s, c)           # arr[i]가 포함되지 않는 경우
        return r1 + r2


t = int(input())

for tc in range(1, t+1) :
    N, K = map(int, input().split())    # 원소의 개수 N, 합 K
    arr = [i for i in range(1, 13)]
    cnt = 0
    cnt = f(0, 12, N, K, 0, 0)
    print(f'#{tc} {cnt}')