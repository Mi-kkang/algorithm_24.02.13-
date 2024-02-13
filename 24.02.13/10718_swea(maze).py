def find(start, endl, n, arr) :
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    i = start[0]
    j = start[1]
    arr[i][j] = -1
    stack = []

    while True :

        for k in range(4) :
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < n and 0 <= nj < n and (arr[ni][nj] == 0 or arr[ni][nj] == 3) :
                stack.append((i, j))
                arr[ni][nj] = -1
                i = ni
                j = nj
                break
        else :
            if stack :
                i, j = stack.pop()
            else :
                break
    if arr[endl[0]][endl[1]] == -1 :
        return True
    else :
        return False


t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    n = int(input())        # n x n 배열 만들기 위한 숫자 n 받기
    arr = [list(map(int, input())) for _ in range(n)]

    st_r = 0
    st_c = 0
    en_r = 0
    en_c = 0

    for i in range(n) :
        for j in range(n) :
            if arr[i][j] == 2 :
                st_r = i
                st_c = j
            elif arr[i][j] == 3 :
                en_r = i
                en_c = j

    start = [st_r, st_c]
    endl = [en_r, en_c]

    if find(start, endl, n, arr) :
        print(f'#{tc} 1')
    else :
        print(f'#{tc} 0')