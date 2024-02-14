def f(i, k) :
    global cnt
    global min_v
    cnt += 1
    if i == k :
        # print(*P)
        s = 0       # 선택한 원소의 합
        for j in range(k) :     # j 행에 대해
            s += arr[j][P[j]]   # j 행에서 P[j] 열을 고른 경우의 합 구하기
        if min_v > s :
            min_v = s

    else :
        for j in range(i, k) :          # P[i] 자리에 올 원소 P[j]
            P[i], P[j] = P[j], P[i]     # P[i] <-> P[j]
            f(i+1, k)
            P[i], P[j] = P[j], P[i]     # 교환전으로 복구



n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
P = [i for i in range(n)]
min_v = 100
cnt = 0
f(0, n)
print(min_v, cnt)