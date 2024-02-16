'''
240213_Stack2_1(3) 의 문제 미로이다.
하지만 큐로 풀어본다!!!
'''

def find_start(N) :
    for i in range(N) :
        for j in range(N) :
            if maze[i][j] == '2' :
                return i, j


def bfs(i, j, N) :                          # i, j 탐색 시작 위치, N 크기
    q = []                                  # 큐 생성
    visited = [[0]*N for _ in range(N)]     # visited 생성
    q.append((i,j))                         # 시작점 인큐
    visited[i][j] = 1                       # 시작점 방문표시
    while q :                               # 남은 칸이 있으면
        i, j = q.pop(0)                     # 방문할 칸 디큐
        if maze[i][j] == '3' :              # 목적지에 도착
            return 1
        for di, dj in[[0,1], [1,0], [0,-1], [-1,0]] :    # i, j에 인접하고 방문하지 않은 경우(큐에 들어있지 않으면)
            ni, nj = i+di, j+dj                         # 인접 후보위치
            # 인접조건 and 큐에 들어있지 않으면
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] !='1' and visited[ni][nj]==0 :
                q.append((ni,nj))                       # 인큐
                visited[ni][nj] = visited[i][j] + 1     # 인큐 되었음 표시

    return 0        # 경로가 없는 경우

t = int(input())
for tc in range(1, t+1) :
    N = int(input())
    maze = [input() for _ in range(N)]

    sti, stj = find_start(N)

    result = bfs(sti, stj, N)

    print(f'#{tc} {result}')