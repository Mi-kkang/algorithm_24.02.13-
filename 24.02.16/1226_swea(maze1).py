di = [0, -1, 0, 1]              # 델타를 쓸거예용~
dj = [1, 0, -1, 0]

def find_spot(g, N, li) :
    for i in range(N) :
        for j in range(N) :
            if maze[i][j] == g :
                li.append(i)
                li.append(j)
                return

def dfs(s, n, g) :      # s는 시작점, n은 배열의 길이, g는 도착점
    q = []              # 큐 생성
    visited = [[0] * N for _ in range(N)]   # 방문을 확인할 배열 생성
    i = s[0]        # 시작점의 좌표 저장
    j = s[1]
    endi = g[0]
    endj = g[1]
    q.append([i, j])    # 인큐
    visited[i][j] = 1   # 방문표시

    while q :           # 큐가 비어있지 않다면 계속 ㄱ
        t = q.pop(0)
        ti = t[0]
        tj = t[1]

        if ti == endi and tj == endj :      # 도착 좌표랑 같다면,
            return 1

        for k in range(4) :
            tdi = ti + di[k]
            tdj = tj + dj[k]

            # 좌표가 배열 안에 있고, 벽이 아니며, 방문한 적 없을 경우,
            if 0<= tdi <N and 0<= tdj <N and maze[tdi][tdj] != 1 and visited[tdi][tdj] == 0 :
                q.append([tdi, tdj])        # 인큐
                visited[tdi][tdj] = visited[ti][tj] + 1     # 방문 누적해주기

    return 0        # 방문할 수 있는 곳은 다 했는데 도착 좌표에 도달하지 못했다면



t = 10                  # 테스트 케이스 10개

for tc in range(1, t+1) :
    tc_n = int(input())     # 테스트 케이스 넘버
    N = 16                  # 행렬의 가로 세로의 길이 N
    maze = [list(map(int,input())) for _ in range(N)]   # 미로를 만들자!
    start = []              # 시작과 끝의 좌표를 넣을 리스트 생성
    end = []

    find_spot(2,N,start)    # 출발점과 도착점의 좌표를 찾자!
    find_spot(3,N, end)

    res = dfs(start, N, end)

    print(f'#{tc_n} {res}')
