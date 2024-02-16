def find_resi(k, n) :           # k는 층수, n은 호실
    global memo
    if k >= 1 and memo[k][n] == 0 :
        for m in range(k+1) :
            for l in range(1, n+1) :
                memo[k][n] += memo[m][l]
    return memo[k][n]
    # if k == 0 :         # 제일 아래층일 경우,
    #     # 저장되어 있는 값은 정해져 있다.
    #     global memo
    #     for i in range(1, n+1) :
    #         memo[k][i] = i
    #     resident = 0
    #
    #
    # else :
    #     ans = 0                     # 원하는 호실에 사는 사람은?
    #     for j in range(1, n+1) :
    #         ans += find_resi(k-1, j)    # 그 아래 사는 사람 중 1~n호실에 사는 사람 수의 합
    #
    #
    # return ans




t = int(input())        # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    k = int(input())    # 아파트 층수 k
    n = int(input())    # 아파트 호실 n

    memo = [[0]*(n+1) for _ in range(k+1)]

    for i in range(1, n+1) :
        memo[0][i] = i

    find_resi(k, n)
    print(memo[k][n])