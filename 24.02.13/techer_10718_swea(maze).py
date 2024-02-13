'''
1
5
13001
10101
10101
10101
10021
'''

def f(i, j, n) :
    stack = []          # 지나간 경로 저장용
    while True :
        maze[i][j] = 1  # 방문한 칸에 표시하기
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]] :
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != 1 : # 미로 내부 and 벽이 아니거나 도착지이면
                if maze[ni][nj] == 3 :
                    return 1
                stack.append((i,j))     # 현재칸 push
                i, j = ni, nj
                break   # for di, dj  / 새 i, j 칸으로 이동
        else :      # 지나온 경로에서 다시 시작해야 하는 경우
            if stack :
                i, j = stack.pop()
            else :
                return 0

t = int(input())
for tc in range(1, t+1) :
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]

    # 시작점 찾기
    sti = stj = -1
    for i in range(n) :
        for j in range(n) :
            if maze[i][j] == 2 :
                sti = i
                stj = j
                break   # for j

        if sti != -1 :
            break       # for i

    # 미로찾기
    result = f(sti, stj, n)
    print(f'#{tc} {result}')