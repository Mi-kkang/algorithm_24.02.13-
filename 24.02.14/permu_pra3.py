def f(i, k, s) :    # s : i-1까지 선택한 원소의 합
    global cnt
    global min_v
    cnt += 1
    if i == k :
        # print(*P)
        if min_v > s :
            min_v = s

    elif s >= min_v :
        return

    else :
        for j in range(i, k) :          # P[i] 자리에 올 원소 P[j]
            P[i], P[j] = P[j], P[i]     # P[i] <-> P[j]
            f(i+1, k, s+arr[i][P[i]])
            P[i], P[j] = P[j], P[i]     # 교환전으로 복구



n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
P = [i for i in range(n)]
min_v = 100
cnt = 0
f(0, n, 0)
print(min_v, cnt)